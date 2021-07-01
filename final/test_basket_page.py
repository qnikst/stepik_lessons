"""
Тесты корзины
"""
import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.catalogue_page import CataloguePage
from .pages.locators import BasketPageLocators
from .pages.i18n import BasketPageI18n

CATALOGUE_LINK = "http://selenium1py.pythonanywhere.com/catalogue"
LINK = "http://selenium1py.pythonanywhere.com/basket/"

@allure.epic("Работа корзины")
class TestBasketPage:
    """
    Тесты управления состоянием корзины
    """

    @pytest.mark.parametrize('qty', ["1", "2", "3"])
    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа заказа товаров")
    @allure.title("Пользователь может изменить кол-во товара вводом в поле")
    @pytest.mark.personal_tests
    def test_change_amount(self, browser, qty):
        """
        Проверяем, что мы можем изменить количество товара на другое значение
        """
        # Arrange
        page = CataloguePage(browser, CATALOGUE_LINK)
        page.open()
        product = page.add_random_product_to_basket()
        page = BasketPage(browser, LINK)
        page.open()
        row = page.load_rows()[0]

        # Act
        row.set_quantity(int(qty))
        row.update_quantity()

        # Assert
        row = page.load_rows()[0]
        actual_price = row.read_total()
        expected_price = product.price * int(qty)
        assert actual_price == expected_price, \
            f"Общая цена товара отличается от ожидаемой. Текущая цена товара {actual_price}, ожидается {qty}*{product.price} = ${expected_price}"

    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа заказа товаров")
    @allure.title("Пользователь может удалить товар из корзины кнопкой")
    @pytest.mark.xfail
    @pytest.mark.personal_tests
    def test_remove_product(self, browser):
        """
        Проверяем, что мы можем удалить товар из корзины
        """
        # Arrange
        page = CataloguePage(browser, CATALOGUE_LINK)
        page.open()
        product = page.add_random_product_to_basket()
        page = BasketPage(browser, LINK)
        page.open()
        row = page.load_rows()[0]

        # Act
        row.delete()

        # Assert
        assert page.is_disappeared(*BasketPageLocators.ITEM_SUBMIT), \
           "Товар должен был быть исчезнуть, а он остался"

@allure.epic("Оформление заказа")
class TestBasketCheckout:
    """
    Тесты оформления заказа
    """

    @allure.feature("Заказ покупки")
    @allure.story("Заказ от анонимного пользователя")
    @allure.title("Анонимный пользователь может оформить заказ")
    @pytest.mark.xfail
    @pytest.mark.personal_tests
    def test_checkout_as_guest(self, browser):
        """
        Проверяем, что мы можем оформить заказ неавторизованным пользователем,
        мы проверяем, что пользователь, если хочет остаться анонимным,
        заполнив форму окажется на странице заполнения адреса
        """
        # Arrange
        page = CataloguePage(browser, CATALOGUE_LINK)
        page.open()
        page.add_random_product_to_basket()
        page = BasketPage(browser, LINK)
        page.open()
        page.checkout()

        # Act
        page.fill_email('user@example.com')
        page.continue_checkout()

        # Assert
        assert page.is_text_present_at(BasketPageLocators.PAGE_SUBHEADER, BasketPageI18n.shipping_address()), \
           "Не произошёл переход на страницу заполнения адреса"
