from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestLoginPage:

    class TestMainPage:
        def test_guest_can_go_to_login_page(self, browser):
            page = LoginPage(browser, link)
            page.open()
            page.should_be_login_page()
