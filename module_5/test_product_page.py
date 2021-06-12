from .pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestProductPage:

    #def test_guest_can_add_product_to_basket(self, browser):
    #    """ Тест проверяет то, что анонимный пользователь может добавить продукт в пустую корзину,
    #    добавление подтверждено и стоимость корзины совпадает с ценой товара.
    #    """
    #    product_page = ProductPage(browser, link)
    #    product_page.open()
    #    (name, cost) = product_page.add_to_basket()
    #    product_page.solve_quiz_and_get_code()
    #    product_page.check_product_to_basket_confirmed(name)
    #    product_page.check_basket_cost(cost+10)

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
