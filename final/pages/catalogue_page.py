"""
Тесты каталога
"""
import random
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators import CataloguePageLocators
from ..utils.parse_page import find_price_at


class ProductData:
    """
    Данные о товаре. Этот чистый объект, который переживает перезагрузку
    страниц сайта
    """

    def __init__(self, price: float, title: str):
        self.price = price
        self.title = title


class Product:
    """
    Обёртка для выбранного продукта. Операции над объектом этого класса
    можно выполнять только пока страница не обновлена.
    """

    def __init__(self, element: WebElement):
        price = find_price_at(element, CataloguePageLocators.PRODUCT_PRICE)
        title = element.find_element(*CataloguePageLocators.PRODUCT_TITLE).text
        self.__element = element
        self.__data = ProductData(price, title)

    @property
    def price(self):
        """
        Цена товара
        :return:  float
        """
        return self.__data.price

    @property
    def title(self):
        """
        Заголовок товара
        :return: str
        """
        return self.__data.title

    @property
    def data(self) -> ProductData:
        """
        Данные о товаре
        :return: ProductData
        """
        return self.__data

    def add_to_basket(self):
        """
        Добавить выбранный товар в корзину
        :return:
        """
        submit_button = self.__element.find_element(*CataloguePageLocators.SUBMIT_BUTTON)
        submit_button.click()


ProductList = list[Product]


class CataloguePage(BasePage):
    """
    PageObject модель для страницы каталога
    """

    def load_products(self) -> ProductList:
        """
        Загрузить список продуктов находящихся на странице
        :return:
        """
        return [Product(x) for x in self.browser.find_elements(*CataloguePageLocators.PRODUCT_ITEM)]

    def add_random_product_to_basket(self) -> ProductData:
        """
        Добавить случайный продукт со страницы в корзину.
        :return: Данные о заказанном продукте.
        """
        products = self.load_products()
        product = random.choice(products)
        product.add_to_basket()
        return product.data
