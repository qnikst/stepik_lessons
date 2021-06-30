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
        Проверяем, что анонимный пользователь может перейти в корзину с главной страницы
        """
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty()

