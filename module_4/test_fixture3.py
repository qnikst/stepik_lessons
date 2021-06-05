import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")
