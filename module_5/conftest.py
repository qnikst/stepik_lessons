"""
Конфигурация для тестов
"""
from datetime import datetime
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """"
    Добавляет разбор параметров коммандной строки
    """
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en, etc.")
    parser.addoption('--take_screenshot', action='store', default=None,
                     help="Add if you want to take screenshot at the end of the test")

@pytest.fixture(scope="session")
def user_language(request):
    """
    Фикстура позволяющая получить доступ к установленному языку пользователя
    """
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language should be set")
    return language.lower()

@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура позволяющая получить доступ объекту браузера. Браузер
    настраивется выбирается по настройке browser_name, устанавливает локаль,
    переданную в настройке language, так же управляет настройками сохранять
    нам скриншот в конце теста или нет.
    """
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language should be set")
    the_browser = None
    if browser_name == "chrome":
        options = Options()
        if not language is None:
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
        the_browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        if not language is None:
            firefox_profile.set_preference("intl.accept_languages", language)
        the_browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield the_browser

    take_screenshot = request.config.getoption("take_screenshot")
    if not take_screenshot is None:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        the_browser.save_screenshot('screenshot-%s.png' % now)
    the_browser.quit()
