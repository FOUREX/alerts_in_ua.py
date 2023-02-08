class InvalidToken(Exception):
    """
    Не дійсний токен
    """


class TooManyRequests(Exception):
    """
    Перевищення ліміту запитів у хвилину (3-4 запити)
    """


class UnknownError(Exception):
    """
    Невідома помилка. Якщо у вас виникла ця помилка, то зв'яжіться з розробником. Telegram: @FOUREX_dot_py
    """
