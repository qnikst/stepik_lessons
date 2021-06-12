from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    __login_page_url = "/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.__login_page_url in self.browser.current_url, \
            self.__login_page_url + " is not present in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented on page"
