"""
Модуль вводит класс BasePage
"""
import allure
import math
import re

from selenium.common.exceptions \
    import NoSuchElementException, NoAlertPresentException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


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

    @allure.step("Переход на страницу логина")
    def go_to_login_page(self):
        """
        Перейти на страницу логина

        @example

            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
        """
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    @allure.step("Переход на страницу корзины")
    def go_to_basket_page(self):
        """
        Перейти на страницу корзины

        @example

            page.go_to_basket_page()
            basket_page = BasketPage(browser, browser.current_url)
        """
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

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

    def should_be_authorized_user(self):
        """
        Проверяет, что пользователь авторизован. В случае провала
        выбрасывает AssertionErrror
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        """
        Проверяет, что на странице доступна ссылка на страницу логина.
        В случае провала выбрасывает исключение
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

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


class wait_for_text_to_match:
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
