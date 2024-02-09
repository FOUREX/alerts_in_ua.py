class BaseAlertsException(Exception):
    error_code: int


class NotAuthorized(BaseAlertsException):
    """
    Токен API відсутній, неправильний, відкликаний або прострочений.
    """

    error_code = 401

    def __init__(self):
        super().__init__("Токен API відсутній, неправильний, відкликаний або прострочений.")


class Forbidden(BaseAlertsException):
    """
    Ваш IP адрес заблокований або API не доступне в вашій країні.
    """

    error_code = 403
    
    def __init__(self):
        super().__init__("Ваш IP адрес заблокований або API не доступне в вашій країні.")


class TooManyRequests(BaseAlertsException):
    """
    Ліміт запитів на хвилину перевищено
    """

    error_code = 429
    
    def __init__(self):
        super().__init__("Ліміт запитів на хвилину перевищено")


class UnknownError(BaseAlertsException):
    """
    Невідома помилка. Якщо у вас виникла ця помилка, то зв'яжіться з розробником. Telegram: @FOUREX_dot_py,
    Email: Foxtrotserega@gmail.com
    """

    def __init__(self, message: str = None):
        if message is None:
            self.message = "Невідома помилка. Якщо у вас виникла ця помилка, то зв'яжіться з розробником."\
                           "Telegram: @FOUREX_dot_py, Email: Foxtrotserega@gmail.com"

        self.message = message

        super().__init__(self.message)
