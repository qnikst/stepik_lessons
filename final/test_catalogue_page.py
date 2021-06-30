"""
Тесты страницы с продуктом
"""
import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
# from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestCataloguePage:
    """
    Тесты страницы продукта
    """

    @allure.story("Просмотр каталога")
    @allure.story("Покупка товара")
    @allure.title("Добавление товара в корзину")
    @pytest.mark.personal
    def test_add_to_basket(self):
        pytest.skip("not yet implemented")

