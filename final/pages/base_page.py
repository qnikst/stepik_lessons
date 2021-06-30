"""
Базовая страница для сайта. Модуль, который используется
для построение PageObject страниц сайта.
"""
import allure

from selenium.common.exceptions \
    import NoSuchElementException, TimeoutException
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

    @allure.step("Открыть страницу")
    def open(self):
        """
        Открыть текущую страницу
        """
        self.browser.get(self.url)

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
        """ Прверяет, что элемента нет на странице

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
