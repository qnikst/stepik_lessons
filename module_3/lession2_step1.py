from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
try:
  browser.get(link)

  num1 = browser.find_element_by_id("num1")
  num2 = browser.find_element_by_id("num2")
  v = str(int(num1.text) + int(num2.text))
  select = Select(browser.find_element_by_id("dropdown"))
  select.select_by_visible_text(v)
  # browser.find_element_by_id("robotCheckbox").click()
  # browser.find_element_by_id("robotsRule").click()
  browser.find_element_by_css_selector("button.btn").click()

  # input1 = browser.find_element_by_tag_name("input")
  # input1.send_keys("Ivan")
  # input2 = browser.find_element_by_name("last_name")
  # input2.send_keys("Petrov")
  # input3 = browser.find_element_by_class_name("city")
  # input3.send_keys("Smolensk")
  # input4 = browser.find_element_by_id("country")
  # input4.send_keys("Russia")
  # button = browser.find_element_by_css_selector("button.btn")
  # button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(30)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла
