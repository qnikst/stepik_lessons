from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
browser = None


def setup_module():
    print("\nstart browser for test suite..")
    global browser
    browser = webdriver.Chrome()


def teardown_module():
    print("quit browser for test suite..")
    browser.quit()


def test_guest_should_see_login_link():
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_basket_link_on_the_main_page():
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")
