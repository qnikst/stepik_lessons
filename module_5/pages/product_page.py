"""
Тесты страницы продукта
"""
import re

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """
    PageObject класс для страницы продукта
    """

    def __parse_price(self, where):
        price_text = self.browser.find_element(*where).text
        search_result = re.search(r"\d+.?\d*", price_text)
        return float(search_result.group(0))

    def add_to_basket(self):
        """ Добавить текущий продукт в корзину
        @returns (name, cost)
            name — название продукта (text)
            cost — цена продукта (float)
        """
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        price = self.__parse_price(ProductPageLocators.PRODUCT_PRICE)
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        return (name, price)

    def check_product_to_basket_confirmed(self, name):
        """ Проверяет наличие уведомления о том, что продукт добавлен в корзину,
        параметром принимает ожидаемое название продукта
        """
        assert self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, f"^{name}$"), \
          f"Отсутсвует подтверждение добавления в корзину, содержащее название продукта ({name})"

    def check_basket_cost(self, expected_cost):
        """ Проверяет, что стоимость корзины соответствует ожиданию
        """
        # Тут я совсем не уверен как сделать лучше, с одной стороны хороший вариант
        # это сделать implicit wait и ждать пока не появится нужный элемент, но тогда
        # в случае дозагрузки страницы мы можем увидеть необновлённый тест и дальнейшие
        # проверки сломаются. Второй вариант это использовать explicit wait, но тогда
        # или мы не сможем добавить красивое сообщение об ошибке (вариант 2), или
        # тест будет содержать ветвления (вариант 3)
        assert self.is_element_present(*ProductPageLocators.BASKET_MINI), \
            "Текущая цена корзины не найдена"
        cost = self.__parse_price(ProductPageLocators.PRODUCT_PRICE)
        assert cost == expected_cost, \
            f"Неожиданная стоимость корзины {cost}, ожидается {expected_cost}"
        # Вариант 2:
        # assert self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, name), \
        #  f"Стоимоть корзины отличается от ожидавшейся ({expected_cost})"
        #
        # Вариант 3
        # found = self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, name)
        # if not found:
        #     cost = self.__parse_price(ProductPageLocators.PRODUCT_PRICE)
        #     assert cost == expected_cost, \
        #         f"Неожиданная стоимость корзины {cost}, ожидается {expected_cost}"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is presented, but should not be"

    def should_success_message_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
          "Success message is presented, but should not be"
