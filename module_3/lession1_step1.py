from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
try:
  browser.get(link)

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)
  browser.find_element_by_id("answer").send_keys(y)
  browser.find_element_by_id("robotCheckbox").click()
  browser.find_element_by_id("robotsRule").click()
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
