"""
Модуль вводит класс BasePage
"""
import math
import re

from selenium.common.exceptions \
    import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
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

    def is_text_present_at(self, where, what, explicit_timeout=12):
        """
        Проверяет является ли текст подстрокой заданного элемента.
        Можно использоват параметр explicit_timeout для того, чтобы
        переопределить время ожиадания по умолчанию

        @returns bool

        @example
        assert self.is_text_present_at(ProductPageLocators.URGENT_SUCCESS_MESSAGES, name), \
          f"Отсутсвует подтверждение добавления в корзину, содержащее название продукта ({name})"
        """
        try:
            WebDriverWait(self.browser, explicit_timeout).until(
                wait_for_text_to_match(where, what))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """
        Удобная функция за авторством авторов курса stepik,
        надеюсь предоставляется как public domain
        """
        alert = self.browser.switch_to.alert
        x_text = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x_text))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


class wait_for_text_to_match(object):
    """
    Expected condition проверяющая, что найденный текст соотвествует паттерну
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
