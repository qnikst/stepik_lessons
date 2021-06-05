from selenium import webdriver
from sys import argv
import time
import unittest


class TestsMy(unittest.TestCase):

  def _generic_test(self, link):
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
      self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "User should register") 
    finally:
        browser.quit()

  def test_registration1(self):
    self._generic_test("http://suninjuly.github.io/registration1.html")

  def test_registration2(self):
    self._generic_test("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
  unittest.main()
