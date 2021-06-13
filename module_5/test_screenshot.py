link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item_page_has_add_basket_button(browser):
    browser.get(link)
    btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn.is_displayed()
