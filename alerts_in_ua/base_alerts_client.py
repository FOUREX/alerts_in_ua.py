from abc import ABC, abstractmethod
from time import time

from alerts_in_ua.locations import Locations
from alerts_in_ua.location import Location


class BaseAlertsClient(ABC):
    SOFT_LIMIT = 3
    HARD_LIMIT = 8

    def __init__(self, token: str, requests_per_minute_limit: int = SOFT_LIMIT):
        """
        Базовий клієнт

        :param token: Токен доступу
        :param requests_per_minute_limit: Ліміт запитів на хвилину
        """

        self._token = token
        self._requests_per_minute_limit = requests_per_minute_limit

        self._url = f"https://api.alerts.in.ua/v1/alerts/active.json"
        self._headers = {"Authorization": f"Bearer {self._token}", "If-Modified-Since": ""}

        self._locations_json: dict = ...
        self._locations: Locations = ...
        self._response_status_code: int = ...

        self._timer = time()
        self._requests_per_minute = 0

    def _make_locations(self):
        if self._response_status_code == 304:
            return

        alerts = self._locations_json["alerts"]
        meta = self._locations_json["meta"]

        locations = Locations(disclaimer=self._locations_json["disclaimer"], last_updated_at=meta["last_updated_at"])

        for alert in alerts:
            location_id = alert["id"]
            location_title = alert["location_title"]
            location_type = alert["location_type"]
            started_at = alert["started_at"]
            finished_at = alert["finished_at"]
            updated_at = alert["updated_at"]
            alert_type = alert["alert_type"]
            location_uid = alert["location_uid"]
            location_oblast = alert["location_oblast"]
            location_raion = None
            notes = alert["notes"]
            calculated = alert["calculated"]

            if "location_raion" in alert:
                location_raion = alert["location_raion"]

            locations.append(
                Location(
                    location_id,
                    location_title,
                    location_type,
                    started_at,
                    finished_at,
                    updated_at,
                    alert_type,
                    location_uid,
                    location_oblast,
                    location_raion,
                    notes,
                    calculated,
                )
            )

        self._locations = locations

    @abstractmethod
    def _make_request(self, force: bool):
        pass

    @abstractmethod
    def get_active_json(self, force: bool = False) -> dict:
        """
        Повертає необроблену відповідь від API у вигляді JSON

        :param force: Примусово робить запит на API ігноруючи ліміт запитів на хвилину (requests_per_minute_limit), але не перевищить hard limit. (Бажано не використовувати)

        :raise InvalidToken: Токен API відсутній, неправильний, відкликаний або прострочений.
        :raise Forbidden: Ваш IP адрес заблокований або API не доступне в вашій країні.
        :raise TooManyRequests: Ліміт запитів на хвилину перевищено
        :raise UnknownError: Невідома помилка
        """

        pass

    @abstractmethod
    def get_active(self, force: bool = False) -> Locations:
        """
        Повертає список місць з тривогою

        :param force: Примусово робить запит на API ігноруючи ліміт запитів на хвилину (requests_per_minute_limit), але не перевищить hard limit. (Бажано не використовувати)

        :raise InvalidToken: Токен API відсутній, неправильний, відкликаний або прострочений.
        :raise Forbidden: Ваш IP адрес заблокований або API не доступне в вашій країні.
        :raise TooManyRequests: Ліміт запитів на хвилину перевищено
        :raise UnknownError: Невідома помилка
        """

        pass
