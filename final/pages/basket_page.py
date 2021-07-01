"""
Тесты корзины
"""
import allure
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators import BasketPageLocators
from ..utils.parse_page import find_price_at


class Row:
    """
    Доступ к ряду с товаром в корзине
    """

    def __init__(self, element: WebElement):
        self.__element = element

    def read_qty(self) -> int:
        """
        Считывает текущее значение количества заказанного товара
        :return:
        """
        qty_input = self.__element.find_element(*BasketPageLocators.ITEM_QTY)
        return int(qty_input.value)

    def read_total(self) -> float:
        """
        Считывает текущее значение общей стоимости товара
        :return:
        """
        return find_price_at(self.__element, BasketPageLocators.ITEM_COL_TOTAL)


    @allure.step("Устанавливаем новое значение количества товара: {qty}")
    def set_quantity(self, qty: int):
        """
        Установить в поле новое значение количества товара
        :param qty: кол-во товара
        :return:
        """
        qty_input = self.__element.find_element(*BasketPageLocators.ITEM_QTY)
        qty_input.clear()
        qty_input.send_keys(str(qty))

    @allure.step("Обновляем текущее значение количества товара")
    def update_quantity(self):
        """
        Обновить количество товара на введённое в поле
        :return:
        """
        self.__element.find_element(*BasketPageLocators.ITEM_SUBMIT).click()

    @allure.step("Удаляем продукт из корзины")
    def delete(self):
        self.__element.find_element(*BasketPageLocators.ITEM_DELETE).click()

RowsList = list[Row]


class BasketPage(BasePage):
    """
    PageObject класс для страницы корзины
    """
    __basket_page_url = "/basket/"

    def should_be_basket_page(self):
        """
        Проверка на то, что это страница конрзины
        """
        assert self.__basket_page_url in self.browser.current_url, \
            self.__basket_page_url + " is not present in current url"

    def should_be_empty(self):
        """
        Проверка на то, что корзина пуста
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине уже есть продукты, хотя это не ожидается"
        assert self.is_text_present_at(BasketPageLocators.CONTENT, "Your basket is empty"), \
            "Отсутствует сообщение о том, что корзина пуста"

    @allure.step("Загружаем список строк в корзине")
    def load_rows(self) -> RowsList:
        """
        Загрузить список рядов
        :return:
        """
        return [Row(x) for x in self.browser.find_elements(*BasketPageLocators.BASKET_ITEM)]

    @allure.step("Переходим на форму оформления заказа")
    def checkout(self):
        """
        Перейти на страницу оформления товара
        :return:
        """
        self.browser.find_element(*BasketPageLocators.CHECKOUT_LINK).click()

    @allure.step("Заполняем email {email}")
    def fill_email(self, email):
        """
        Заполнить email на форме
        :return:
        """
        self.browser.find_element(*BasketPageLocators.USERNAME_ID).send_keys(email)

    @allure.step("Отправляем форму идентификации")
    def continue_checkout(self):
        """
        Заполнить email на форме
        :return:
        """
        self.browser.find_element(*BasketPageLocators.CONTINUE_CHECKOUT).click()
