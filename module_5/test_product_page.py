import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestProductPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page() 
        login_page = LoginPage(browser, browser.current_url); 
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.parametrize('promo_offer', 
        ["offer0","offer1","offer2","offer3","offer4","offer5","offer6",
          pytest.param("offer7",marks=pytest.mark.xfail),
         "offer8","offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        product_page = ProductPage(browser, link + "/?promo=" + promo_offer)
        product_page.open()
        (name, cost) = product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_product_to_basket_confirmed(name)
        product_page.check_basket_cost(cost)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_not_see_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_see_success_message()
 
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_success_message_dissapear()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page() 
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty()

@pytest.mark.user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = login_page.generate_unique_email()
        login_page.register_new_user(email, "qazwsx3edcrfv")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_see_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link + "/?promo=offer0")
        product_page.open()
        (name, cost) = product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_product_to_basket_confirmed(name)
        product_page.check_basket_cost(cost)
