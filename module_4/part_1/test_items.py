"""
Тесты проверяющие правильность настройки локали на сайте.
"""
import urllib.parse
import pytest

# Список текстов кнопок в зависимости от локали сайта
BASKET_MESSAGE_BY_SITE_LOCALE = {
  'ru': 'Добавить в корзину',
  'en-gb': 'Add to basket',
  'es': 'Añadir al carrito',
  'fr': 'Ajouter au panier'
  }

# Note_to_reviewer:
#  Скорее всего тут нужна более хитрая функция, убирающая регион и доп опции и возвращающая
#  регион для исключений, вроде en-GB
"""
Отображение локали браузера на локаль сайта. По хорошему, несколько
локалей браузера могут отоборажаться в одну локаль сайта, например,
все en-* отображаются в en-gb на сайте.
"""
LOCALE_MAPPINGS = {
  'es': 'es',
  'fr': 'fr',
  'ru': 'ru',
  'en-gb': 'en-gb',
  }

class UnknownLanguage(Exception):
    """
    Exception raised when we have not defined the language yet

    Attributes:
      language -- the name of the unknown language
    """

    def __init__(self, language):
        super().__init__()
        self.language = language


# Note_to_reviewer: в этом тесте мы передаём параметр user_language через фикстуру, поскольку
# нам надо знать, что ожидать на сайте, возможно есть более аккуратные способы
# это сделать.
#
# Я бы ещё запретил передавать ненастроенные локали..
# @pytest.mark.xfail("not config.getvalue('language') in SUPPORTED_LANGUAGES")
def test_add_button_has_correct_text_by_locale(browser, user_language):
    """
    Проверяем, что текст на кновке добавления в корзину правильный, при этом нам важна
    только локаль пользователя, которая передана через опции теста и мы не смотрим
    на локаль сайта.
    """
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    add_to_basket_button_selector = "button.btn-add-to-basket"
    if not user_language in LOCALE_MAPPINGS[user_language]:
        raise UnknownLanguage(user_language)
    expected_text = BASKET_MESSAGE_BY_SITE_LOCALE[LOCALE_MAPPINGS[user_language]]

    # Arrange
    browser.get(link)
    button = browser.find_element_by_css_selector(add_to_basket_button_selector)
    current_text = button.text

    # Act

    # Assert
    assert current_text == expected_text, \
      f'Текст на копке должен быть {expected_text}, а там: {current_text}'

# Note_to_reviewer:
#
# Я тут хотел бы сделать что-то вроде
#
#   @pytest.mark.xfail(raises=UnknownLanguage)
#
# Для того, чтобы явно отмечать неподдерживаемые локали, но кажется это невозможно.
# Самое близкое, что у меня получилось это ввести константу
#
#   SUPPORTED_LANGUAGES = ['ru', 'en']
#
# и маркировку:
#
#   @pytest.mark.xfail("not config.getvalue('language') in SUPPORTED_LANGUAGES")
#
# Но у этого подхода есть минусы, нам приходится заполнять данные в двух местах,
# мы привязываемся к языкам из передаваемых в accept-language, это приведёт к двум
# проблемам:
#
#   1. Мы не сможем передавать несколько языков сразу
#   2. Мы не поддержим случай, если несколько языков отображаются в одну локаль сайта
#
# Поэтому придётся жить с падением теста на неизвестных языках
#
# Этот тест, мне лично кажется более удобным, поскольку мы в него не передаём настройки
# пользователя и работаем с браузером как он уже настроен. Но такой тест не заработает
# при автоматической проверке по условиям на сайте stepik, поэтому его отключаю.
@pytest.mark.skip(reason="Кажется этот тест делает не то, что просится в задаче")
def test_add_button_has_correct_text_by_path(browser):
    """
    Проверяем, что текст на кновке добавления в корзину правильный.
    **Важно** В этом тесте мы уже предполагаем, что логика определения локали
    сайта по локали браузера работает верно.
    Поэтому мы проверяем, что текст кнопки соотвествует локали сайта.
    """
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    add_to_basket_button_selector = "button.btn-add-to-basket"

    # Arrange
    browser.get(link)
    button = browser.find_element_by_css_selector(add_to_basket_button_selector)
    url_path = urllib.parse.urlparse(browser.current_url).path
    # Act

    # Мы определяем язык по строке браузера, на странице, которой мы находися
    #  напр. http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/
    #                                               ^
    #                                               +--- русская локаль
    #
    # Assert
    locale = url_path.split(sep="/")[1]
    current_text = button.text
    if not locale in BASKET_MESSAGE_BY_SITE_LOCALE:
        raise UnknownLanguage(locale)
    expected_text = BASKET_MESSAGE_BY_SITE_LOCALE[locale]
    assert current_text == expected_text, \
        f'Текст на копке должен быть {expected_text}, а там: {current_text}'
