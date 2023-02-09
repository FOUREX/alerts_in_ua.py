import requests

from alerts_in_ua.location import Location
from alerts_in_ua.locations import Locations
from alerts_in_ua.exceptions import InvalidToken, TooManyRequests, UnknownError


class AlertsClient:
    def __init__(self, token: str, dev: bool = False):
        """
        Клієнт. Дані беруться з сайту "alerts_in_ua.in.ua"

        :param token: Токен доступу
        :param dev: Використання тестового сервера
        """

        self.__token = token

        self.__url = f"https://{'dev-' if dev else ''}api.alerts.in.ua/v1/alerts/active.json"
        self.__headers = {"Authorization": f"Bearer {self.__token}"}

        self.__locations = ...

    def get_active(self) -> Locations:
        """
        Повертає список місць з тревогою

        :raise InvalidToken: Не дійсний токен
        :raise TooManyRequests: Забагато запитів
        :raise UnknownError: Невідома помилка
        """

        response = requests.get(url=self.__url, headers=self.__headers)
        data = response.json()

        match response.status_code:
            case 200:
                pass
            case 304:
                return self.__locations
            case 401:
                raise InvalidToken("API token required. Please contact api@alerts_in_ua.in.ua for details.")
            case 429:
                raise TooManyRequests("API Reach Limit. You should call API no more than 3-4 times per minute")
            case _:
                if "message" not in response.json():
                    raise UnknownError("Unknown error. Please contact the developer. Telegram: @FOUREX_dot_py")
                raise UnknownError(response.json()["message"])

        _alerts = data["alerts"]
        _meta = data["meta"]

        self.__locations = Locations(disclaimer=data["disclaimer"], last_updated_at=_meta["last_updated_at"])

        for alert in _alerts:
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

            location = Location(
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
            self.__locations.append(location)

        return self.__locations
