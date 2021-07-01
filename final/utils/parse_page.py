"""
Набор вспомогательных функций для парсинга произвольной страницы
сайта.
"""
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

Locator = tuple[By, str]


def find_price_at(where: WebElement, what: Locator):
    """
    Находит цену в указанном месте страницы сайта.
    *N.B.* Функция не поддерживает локали и предполагает, что точка это разделитель
    десятичных знаков и отсутствует разделитель разрядов

    :param where: Объект, в контексте которого мы ищем цену
    :param what: Локатор элемента, в котором хранится цена
    :return: float цену товара
    """
    price_text = where.find_element(*what).text
    search_result = re.search(r"\d+.?\d*", price_text)
    return float(search_result.group(0))
