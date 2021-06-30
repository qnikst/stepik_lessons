"""
Тесты страницы с продуктом
"""
import allure
import pytest

LINK = "http://selenium1py.pythonanywhere.com/catalogue"


@allure.epic("Работа каталога")
class TestCataloguePage:
    """
    Тесты каталога
    """

    @allure.feature("Добавление в корзину")
    @allure.title("Пользователь может добавить товар в корзину")
    @pytest.mark.personal
    def test_add_to_basket(self):
        """
        Тест проверяет, что пользователь может добавить продукт
        со страницы, которую видит
        """
        pytest.skip("not yet implemented")
