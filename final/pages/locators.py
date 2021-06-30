"""
Набор локаторов для сайта
"""

# pylint очень огорчается
from selenium.webdriver.common.by import By

class BasePageLocators:
    """
    Локаторы подходящие для всех страниц
    """
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success div.alertinner")

class CataloguePageLocators:
    """
    Локаторы для страницы каталога
    """
    PRODUCT_ITEM = (By.CSS_SELECTOR, "article.product_pod")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h3 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_price p.price_color")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")
    BASKET_MINI = (By.CSS_SELECTOR, "header div.basket-mini")

