"""
Тесты страницы с продуктом
"""
import allure
import pytest
import random

from .pages.catalogue_page import CataloguePage
from .pages.i18n import CataloguePageI18n
from .pages.locators import BasePageLocators

LINK = "http://selenium1py.pythonanywhere.com/catalogue"


@allure.epic("Работа каталога")
class TestCataloguePage:
    """
    Тесты каталога
    """

    @allure.feature("Добавление в корзину")
    @allure.title("Отображается подтверждение при добавлении в продукта в корзину")
    @pytest.mark.personal
    def test_add_to_basket_confirmed(self, browser):
        """
        Тест проверяет, что при добавлении пользователем товара в корзину
        будет отображено сообщение об успехе добавления
        """
        # Arrange
        page = CataloguePage(browser, LINK)
        page.open()
        products = page.load_products()
        product = random.choice(products)
        product_title = product.title

        # Act
        product.add_to_basket()

        # Assert
        assert page.is_text_present_at(BasePageLocators.SUCCESS_MESSAGE,
                                       CataloguePageI18n.make_confirmation_text(product_title)), \
            f"Не появилось уведомление об успешном добавлении продукта {product_title}"

    @allure.feature("Добавление в корзину")
    @allure.title("Цена товаров находящихся в корзине меняется на цену товара")
    @pytest.mark.personal
    def test_add_to_basket_updated_price(self, browser):
        """
        Тест проверяет, что при добавлении пользователем товара в корзину
        стоимость корзины изменяется
        """
        # Arrange
        page = CataloguePage(browser, LINK)
        page.open()

        # Act
        product = page.add_random_product_to_basket()

        # Assert
        actual_price = page.read_basket_price()
        expected_price = product.price
        assert actual_price == expected_price, \
            f"Цена корзины должна быть {expected_price}, а она {actual_price}"
