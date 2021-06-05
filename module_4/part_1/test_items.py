import time
import urllib.parse

# Список сообщений в зависимости от языка, который должен использоваться
# на кнопке добавления в корзину:
MESSAGES = {
  'ru': 'Добавить в корзину',
  'en-gb': 'Add to basket'
  }

def test_add_button_has_correct_text(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    add_to_basket_button_selector = "button.btn-add-to-basket"

    browser.get(link)

    button = browser.find_element_by_css_selector(add_to_basket_button_selector)
    # Мы определяем язык по строке браузера, на странице, которой мы находися
    #  напр. http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/ 
    url_path = urllib.parse.urlparse(browser.current_url).path
    locale = url_path.split(sep="/")[1]
    current_text = button.text
    expected_text = MESSAGES[locale]
    assert current_text == expected_text, f'Текст на копке должен быть {expected_text}, а там: {current_text}'

