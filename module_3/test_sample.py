from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import datetime;

# Вспомогательные функции

def generate_unique_email():
  """
  Сгенерировать уникальный email. Email получается добавлением секции "+<uniq>"
  в email. Это позволит получает письма на основной email, но при этом система
  будет считать email разными (с высокой вероятностью).
  """
  uniq = int(datetime.datetime.now().timestamp())
  return "alexander.vershilov+" + str(uniq) + "@gmail.com"

class LoginPage:

  """
  Страница входа
  """
  _login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

  def __init__(self, browser):
    browser.get(self._login_page_link)

    # При создании объекта браузер переходит на страницу логина, что кажется весьма неправильным,
    # скорее всего мы тут должны создавать локальный браузер, который будет доступен тут и в других
    # объектах страницы, правда тогда непонятно, как правильно быть в случае, если мы переходим
    # на другую страницу, например при сабмите формы.
    self.login_form = LoginForm(browser)

class LoginForm:
  """
  Форма логина
  """
  _registration_email_locator = "#id_registration-email"
  _registration_password_locator = "#id_registration-password1"
  _confirmation_password_locator = "#id_registration-password2"
  _register_button_locator = "button[name='registration_submit']"

  def __init__(self, browser):
      self.email_input = browser.find_element_by_css_selector(self._registration_email_locator)
      self.pass_input = browser.find_element_by_css_selector(self._registration_password_locator)
      self.confirm_pass_input = browser.find_element_by_css_selector(self._confirmation_password_locator)
      self.submit_btn = browser.find_element_by_css_selector(self._register_button_locator)

  def submit(self):
      self.submit_btn.click()



"""
Классы плохих паролей:
"""
BAD_PASSWORD_CLASSES = {
    'too_short':
     { 'example':'wsx3edc'
     , 'message': 'This password is too short. It must contain at least 9 characters'
     }
  , 'too_common':
     { 'example':'123456789'
     , 'message': 'This password is too common.'
     }
  }


def test_register_user_success():
  """
  1.1.1 Тест проверяет успешную регистрацию.

  Подробное описание теста см. в module_1/tests.txt
  """
  # Data
  logout_icon_locator = "ul.nav.navbar-nav.navbar-right a i.icon-signout"
  profile_icon_locator = "ul.nav.navbar-nav.navbar-right a i.icon-user"

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
     login_page = LoginPage(browser)
     login_form = login_page.login_form;

     # Act
     login_form.email_input.send_keys(email)
     login_form.pass_input.send_keys(ideal_password)
     login_form.confirm_pass_input.send_keys(ideal_password)
     login_form.submit()

     # Assert
     WebDriverWait(browser, allowed_timeout_seconds).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, ok_icon_locator)))
     logout_links = browser.find_elements_by_css_selector(logout_icon_locator)
     logout_links_count = len(logout_links)
     assert logout_links_count == 1, f"There should be a single logout link on the page, got {logout_links_count}"
     profile_links = browser.find_elements_by_css_selector(profile_icon_locator)
     profile_links_count = len(profile_links)
     assert profile_links_count == 1, f"There should be a single logout link on the page, got {profile_links_count}"

  finally:
     browser.quit()


def test_register_user_failure_password(password_class):
  # data
  browser = webdriver.Chrome()
  # Не рабоатает:
  # error_message_selector = "div.form-group.has-error #id_registration-password2 + span.error-block"
  error_message_selector = "div.form-group.has-error span.error-block"
  allowed_timeout_seconds = 10
  password = BAD_PASSWORD_CLASSES[password_class]['example'];
  message = BAD_PASSWORD_CLASSES[password_class]['message'];
  email = generate_unique_email()
  try:
     # Arrange
     browser.implicitly_wait(5)
     login_page = LoginPage(browser)
     login_form = login_page.login_form;

     # Act
     login_form.email_input.send_keys(email)
     login_form.pass_input.send_keys(password)
     login_form.confirm_pass_input.send_keys(password)
     login_form.submit()

     # Assert
     WebDriverWait(browser, allowed_timeout_seconds).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, error_message_selector)))

     WebDriverWait(browser, 1).until(
       EC.text_to_be_present_in_element((By.CSS_SELECTOR, error_message_selector), message))

  finally:
     browser.quit()

test_register_user_success()
test_register_user_failure_password('too_short')
test_register_user_failure_password('too_common')
