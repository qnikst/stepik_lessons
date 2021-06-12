"""
Набор локаторов для сайта
"""

# pylint очень огорчается
from selenium.webdriver.common.by import By

class MainPageLocators():
    """
    Локаторы главной сраницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    """
    Локаторы сраницы логина
    """
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    """
    Локаторы сраницы продукта
    """
    PRODUCT_TITLE = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page div.product_main p.price_color")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    URGENT_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages .alert-success div.alertinner strong")
    URGENT_INFO_MESSAGES = (By.CSS_SELECTOR, "#messages .alert-info div.alertinner strong")
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini")
    LOADER = (By.CSS_SELECTOR, "#loader")
