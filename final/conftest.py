import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose language: ru, en, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
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
    yield the_browser
    allure.attach(
        the_browser.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
    the_browser.quit()


@pytest.fixture(scope="session")
def user_language(request):
    """
    Фикстура позволяющая получить доступ к установленному языку пользователя
    """
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language should be set")
    return language.lower()
