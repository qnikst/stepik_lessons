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

class BasketPageLocators():
    """
    Локаторы для корзины
    """
    CONTENT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items  div.row")
    ITEM_QTY = (By.CSS_SELECTOR, "div.checkout-quantity input")
    ITEM_SUBMIT = (By.CSS_SELECTOR, 'div.checkout-quantity button[type="submit"]')
    ITEM_COL_PRICE = (By.CSS_SELECTOR, 'div.col-sm-1')
    ITEM_COL_TOTAL = (By.CSS_SELECTOR, 'div.col-sm-2 p.price_color')
    ITEM_DELETE = (By.CSS_SELECTOR, 'a[data-behaviours="remove"]')
    CHECKOUT_LINK = (By.CSS_SELECTOR, '.clearfix a.btn-primary')
    USERNAME_ID = (By.CSS_SELECTOR, '#id_username')
    PAGE_SUBHEADER = (By.CSS_SELECTOR, 'div.sub-header h1')
    CONTINUE_CHECKOUT = (By.CSS_SELECTOR, 'button[type="submit"]')

