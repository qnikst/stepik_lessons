"""
Тесты корзины
"""
from .base_page import BasePage
from .locators import BasketPageLocators


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
            "Отсутсвует сообщение о том, что корзина пуста"
