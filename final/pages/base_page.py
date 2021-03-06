"""
Базовая страница для сайта. Модуль, который используется
для построение PageObject страниц сайта.
"""
import allure
import re

from selenium.common.exceptions \
    import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage - объект, который наследуют все страницы, содержит
    стандартную библиотеку для наших тестов.
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открыть текущую страницу
        """
        self.__open(self.url)

    @allure.step("Переходим на страницу: {url}")
    def __open(self, url):
        self.browser.get(url)

    def is_element_present(self, how, what):
        """
        Проверяет находится ли элемент на странице. Метод полагается на
        параметр класса timeout и будет ожидать это время.

        @returns bool - значение существует ли искомый элемент или нет.:w

        @example
           self.is_element_present(*LoginPageLocators.LOGIN_FORM)

        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """ Проверяет, что элемента нет на странице

        @returns bool

        @example
        def should_not_be_success_message(self):
           assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
             "Success message is presented, but should not be"
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что элемент исчезает со страницы за указанное время.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    @allure.step("Проверяем, что текст {what} присутствует в {where}")
    def is_text_present_at(self, where, what, explicit_timeout=12):
        """
        Проверяет является ли текст подстрокой заданного элемента.
        Можно использовать параметр explicit_timeout для того, чтобы
        переопределить время ожидания по умолчанию

        @returns bool

        @example
        assert self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, name), \
          f"Отсутствует подтверждение добавления в корзину, содержащее название продукта ({name})"
        """
        try:
            WebDriverWait(self.browser, explicit_timeout).until(
                wait_for_text_to_match(where, what))
        except TimeoutException:
            return False
        return True


class wait_for_text_to_match:
    """
    Expected condition проверяющая, что найденный текст соответствует паттерну
    """

    def __init__(self, locator, pattern):
        self.locator = locator
        self.pattern = re.compile(pattern)

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).text
            return self.pattern.search(element_text)
        except StaleElementReferenceException:
            return False
