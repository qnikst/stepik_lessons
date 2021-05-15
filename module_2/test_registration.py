from selenium import webdriver
from sys import argv
import time

script_name, link = argv

browser = webdriver.Chrome()
try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    first_name.send_keys("Name")
    last_name = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    last_name.send_keys("Surname")
    email = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    email.send_keys("email")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()