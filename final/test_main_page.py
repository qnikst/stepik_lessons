"""
Тесты главной страницы
"""
import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    """
    Тесты главной страницы
    """

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """
        Проверяем, что анонимный пользователь может перейти в конзину с главной страницы
        """
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    """
    Тесты логина с главной стрианицы
    """

    def test_guest_can_go_to_login_page(self, browser):
        """
        Проверяем, что анонимный пользователь может перейти
        на страницу логина
        """
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Проверяем, что анонимный пользователь видит ссылку
        на страницу логина
        """
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()
