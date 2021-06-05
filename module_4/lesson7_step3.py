import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

links = [
    "https://stepik.org/lesson/236895/step/1"
   , "https://stepik.org/lesson/236896/step/1"
   , "https://stepik.org/lesson/236897/step/1"
   , "https://stepik.org/lesson/236898/step/1"
   , "https://stepik.org/lesson/236899/step/1"
   , "https://stepik.org/lesson/236903/step/1"
   , "https://stepik.org/lesson/236904/step/1"
   , "https://stepik.org/lesson/236905/step/1"
  ]

def answer():
    return math.log(int(time.time()))

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    area = browser.find_element_by_css_selector(".string-quiz__textarea")
    area.send_keys(str(answer()));
    btn = browser.find_element_by_css_selector(".submit-submission")

    
    btn.click()

    hint_selector = ".smart-hints__hint"
    WebDriverWait(browser, 1).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, hint_selector)))
    hint = browser.find_element_by_css_selector(hint_selector)
    t = hint.text
    assert t == "Correct!", t
