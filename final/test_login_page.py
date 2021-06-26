"""
Тесты страницы логина
"""
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class TestLoginPage:
    """
    Тесты страницы логина
    """

    def test_guest_can_go_to_login_page(self, browser):
        """
        Тест проверяющий, что страница логина действитейльно таковой
        и является
        """
        page = LoginPage(browser, LINK)
        page.open()
        page.should_be_login_page()
