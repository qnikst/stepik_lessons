"""
Тесты корзины
"""
import allure
import pytest

@allure.epic("Работа корзины")
class TestBasketPage:
    """
    Тесты управления состоянием корзины
    """

    @pytest.mark.personal
    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа слайдера")
    @allure.title("Пользователь может увеличить кол-во товара кнопкой на слайдере")
    def test_increase_amount_slider(self):
        """
        Проверяем, что мы можем увеличить количество заказанного товара слайдером
        """
        pytest.skip("not yet implemented")

    @pytest.mark.personal
    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа слайдера")
    @allure.title("Пользователь может уменьшить кол-во товара кнопкой на слайдере")
    def test_descrease_amount_slider(self):
        """
        Проверяем, что мы можем уменьшить количество заказанного товара слайдером
        """
        pytest.skip("not yet implemented")

    @pytest.mark.parametrize('count', ["0", "1", "42"])
    @pytest.mark.personal
    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа заказа товаров")
    @allure.title("Пользователь может изменить кол-во товара вводом в поле")
    def test_change_amount(self, count):
        """
        Проверяем, что мы можем изменить количество товара на другое значение
        """
        pytest.skip("not yet implemented")

    @pytest.mark.personal
    @allure.feature("Управление товаром в корзине")
    @allure.story("Работа заказа товаров")
    @allure.title("Пользователь может удалить товар из корзины кнопкой")
    def test_remove_product(self):
        """
        Проверяем, что мы можем удалить товар из корзины
        """
        pytest.skip("not yet implemented")


@allure.epic("Оформление заказа")
class TestBasketCheckout:
    """
    Тесты оформления заказа
    """

    @pytest.mark.personal
    @allure.feature("Заказ покупки")
    @allure.story("Заказ от авторизованного пользователя")
    @allure.title("Авторизованной пользователь может оформить заказ")
    def test_checkout_basket(self):
        """
        Проверяем, что мы можем оформить заказ авторизованным пользователем
        """
        pytest.skip("not yet implemented")

    @pytest.mark.personal
    @allure.feature("Заказ покупки")
    @allure.story("Заказ от анонимного пользователя")
    @allure.title("Анонимный пользователь может оформить заказ")
    def test_checkout_as_guest(self):
        """
        Проверяем, что мы можем оформить заказ неавторизованным пользователем
        """
        pytest.skip("not yet implemented")
