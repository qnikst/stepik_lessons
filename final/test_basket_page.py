"""
Тесты корзины
"""
import allure
import pytest

class TestBasketPage:

    @allure.story("Покупка товара")
    @allure.title("Увеличение количества товара в корзине")
    @pytest.mark.personal
    def test_increase_product_amount(self):
        pytest.skip("not yet implemented")

    @allure.story("Покупка товара")
    @allure.title("Заказ товара")
    @pytest.mark.personal
    def test_checkout_basket(self):
        pytest.skip("not yet implemented")
