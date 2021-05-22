from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
try:
  browser.get(link)

  browser.find_element_by_name("firstname").send_keys("Alexander")
  browser.find_element_by_name("lastname").send_keys("Vershilov")
  browser.find_element_by_name("email").send_keys("alexader.vershilov@lalala.com")
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'file.txt')
  e = browser.find_element_by_id("file")
  print(e)
  e.send_keys(file_path)
  button = browser.find_element_by_css_selector("button.btn")
  button.click()
except Exception as e:
  print(e)

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(30)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла
