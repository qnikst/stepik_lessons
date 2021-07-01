# TODO: добавить поддержку генерации текста в зависимости от текущей локали


class CataloguePageI18n:
    """
    Тексты относящиеся к странице каталога.
    """

    @staticmethod
    def make_confirmation_text(product_name):
        """
        Сгенерировать текст, который появляется при подтверждении добавления
        товара в корзину.
        """
        return f'{product_name} has been added to your basket'


class BasketPageI18n:
    """
    Тексты на страницы корзины
    """

    @staticmethod
    def shipping_address():
        return "Shipping address"