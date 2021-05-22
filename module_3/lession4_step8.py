from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
  browser.get("http://suninjuly.github.io/explicit_wait2.html")
  WebDriverWait(browser, 12).until(
          EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
  print("ok")
  button = browser.find_element_by_id("book")
  button.click()

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)
  browser.find_element_by_id("answer").send_keys(y)
  button = browser.find_element_by_id("solve")
  button.click()
except Exception as e:
  print(e)
finally:
  time.sleep(30)
  browser.exit()
