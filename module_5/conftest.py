from datetime import datetime
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en, etc.")
    parser.addoption('--take_screenshot', action='store', default=None,
                     help="Add if you want to take screenshot at the end of the test")

@pytest.fixture(scope="session")
def user_language(request):
    user_language = request.config.getoption("language")
    if user_language is None:
        raise pytest.UsageError("--language should be set")
    return user_language.lower()

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if user_language is None:
        raise pytest.UsageError("--language should be set")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        if not user_language is None:
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        if not user_language is None:
            fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    
    take_screenshot = request.config.getoption("take_screenshot")
    if not take_screenshot is None:
        # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
        browser.save_screenshot('screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()
