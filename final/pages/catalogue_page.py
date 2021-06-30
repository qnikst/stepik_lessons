"""
Тесты каталога
"""
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators import CataloguePageLocators
from ..utils.parse_page import find_price_at


class Product:
    """
    Обёртка для выбранного продукта. Операции над объектом этого класса
    можно выполнять только пока страница не обновлена.
    """

    def __init__(self, browser, element: WebElement):
        price = find_price_at(element, CataloguePageLocators.PRODUCT_PRICE)
        title = element.find_element(*CataloguePageLocators.PRODUCT_TITLE).text
        self.__element = element
        self.price = price
        self.title = title

    def add_to_basket(self):
        """
        Добавить выбранный товар в корзину
        :return:
        """
        submit_button = self.__element.find_element(*CataloguePageLocators.SUBMIT_BUTTON)
        submit_button.click()


class CataloguePage(BasePage):
    """
    PageObject модель для страницы каталога
    """

    def load_products(self):
        return [Product(self.browser, x) for x in self.browser.find_elements(*CataloguePageLocators.PRODUCT_ITEM)]
