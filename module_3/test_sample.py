from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import datetime;

# Сгенерировать уникальный email. Email получается добавлением секции "+<uniq>"
# в email. Это позволит получает письма на основной email, но при этом система
# будет считать email разными (с высокой вероятностью).
def generate_unique_email():
  uniq = int(datetime.datetime.now().timestamp())
  return "alexander.vershilov+" + str(uniq) + "@gmail.com"

# 1.1.1 Тест проверяет успешную регистрацию.
# 
# Подробное описание теста см. в module_1/tests.txt
def test_successful_user_registration():
  # Data
  login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
  registration_email_locator = "#id_registration-email"
  registration_password_locator = "#id_registration-password1"
  confirmation_password_locator = "#id_registration-password2"
  register_button_locator = "button[name='registration_submit']"
  logout_icon_locator = "ul.nav.navbar-nav.navbar-right a i.icon-signout"
  profile_icon_locator = "ul.nav.navbar-nav.navbar-right a i.icon-user1"

  ok_icon_locator = ".alert.alert-success i.icon-ok-sign"
  email = generate_unique_email()
  # Пароль удовлетворяющий требованиям безопасности
  # (лежащий в открытом репозитории, ха-ха)
  ideal_password = "qazwsx+123456"

  # Если нам приходится ждать обработки формы дольше, чем это значение,
  # то мы считаем это багом бека.
  allowed_timeout_seconds = 20

  browser = webdriver.Chrome() 
  
  try:
     # Arrange
     browser.implicitly_wait(5)
     browser.get(login_page_link)
     email_input = browser.find_element_by_css_selector(registration_email_locator)
     pass_input = browser.find_element_by_css_selector(registration_password_locator)
     confirm_input = browser.find_element_by_css_selector(confirmation_password_locator)
     submit_btn = browser.find_element_by_css_selector(register_button_locator)

     # Act
     email_input.send_keys(email)
     pass_input.send_keys(ideal_password)
     confirm_input.send_keys(ideal_password)
     print(submit_btn)
     submit_btn.click()
     
     # Assert

     # XXX: Хорошо-ли, что мы не используем assert здесь? В принцпе функция выбросит
     # исключение, если элемент не появится. Можно ещё проверять по тексту, но тогда
     # тест будет зависеть от локали.
     WebDriverWait(browser, allowed_timeout_seconds).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, ok_icon_locator)))
     # Ну ладно, добавим пару ассертов..
     logout_links = browser.find_elements_by_css_selector(logout_icon_locator)
     logout_links_count = len(logout_links)
     assert logout_links_count == 1, f"There should be a single logout link on the page, got {logout_links_count}"
     profile_links = browser.find_elements_by_css_selector(profile_icon_locator)
     profile_links_count = len(profile_links)
     assert profile_links_count == 1, f"There should be a single logout link on the page, got {profile_links_count}"
     
  finally:
     browser.quit()
     
test_successful_user_registration()
