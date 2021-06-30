"""
Тесты страницы логина
"""
import allure
import pytest
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


@allure.story("Логин и регистрация пользователя")
class TestLoginRegistration:
   """Тесты регистрации пользователя"""

   @allure.title("Успешная регистрация")
   def test_guest_can_register(self, browser):
       """
       Пользователь может успешно зарегистрироваться на сайте
       :param browser:
       :return:
       """
       pytest.skip("not yet implemented")

   @allure.story("Покупка товара")
   @allure.title("Успешный логин")
   def test_guest_can_login(selfs, browser):
      pytest.skip("not yet implemented")

