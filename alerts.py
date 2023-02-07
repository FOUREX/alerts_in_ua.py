import requests


class Location:
    def __init__(self,
                 id: int,
                 location_title: str,
                 location_type: str,
                 started_at: str,
                 finished_at: str,
                 updated_at: str,
                 alert_type: str,
                 location_uid: str,
                 location_oblast: str,
                 location_raion: str,
                 notes: str,
                 calculated: bool):
        self.id = id
        self.location_title = location_title
        self.location_type = location_type
        self.started_at = started_at
        self.finished_at = finished_at
        self.updated_at = updated_at
        self.alert_type = alert_type
        self.location_uid = location_uid
        self.location_oblast = location_oblast
        self.location_raion = location_raion
        self.notes = notes
        self.calculated = calculated

    def __repr__(self):
        return f"Location(id: {self.id}, location_title: {self.location_title}, location_type: {self.location_type}, " \
               f"started_at: {self.started_at}, finished_at: {self.finished_at}, updated_at: {self.updated_at}, " \
               f"alert_type: {self.alert_type}, location_uid: {self.location_uid}, " \
               f"location_oblast: {self.location_oblast}, location_raion: {self.location_raion}, " \
               f"notes: {self.notes}, calculated: {self.calculated})"


class Locations(list):
    def __init__(self, *__locations: Location, disclaimer: str, last_updated_at: str):
        super(Locations, self).__init__(__locations)

        self.disclaimer = disclaimer
        self.last_updated_at = last_updated_at
        self.type = "full"  # Ну потому что v1

    def append(self, __location: Location) -> None:
        super(Locations, self).append(__location)

    def filter(self, **filters) -> list[Location]:
        def location_filter(location: Location):
            for _filter in filters:
                if getattr(location, _filter) != filters[_filter]:
                    return False
            return True

        return list(filter(location_filter, self))


class AlertsClient:
    def __init__(self, token: str, dev: bool = False):
        self.__token = token

        self.__url = f"https://{'dev-' if dev else ''}api.alerts.in.ua/v1/alerts/active.json"
        self.__headers = {"Authorization": f"Bearer {self.__token}"}

        self.locations = ...
        self.requests_per_minute = 0
        self.timer = 0

    def get_active(self) -> Locations:
        response = requests.get(url=self.__url, headers=self.__headers)

        match response.status_code:
            case 200:  # Успішний запит
                pass
            case 304:  # Дані не було змінено
                pass
            case 401:  # Не вказаний, неправильний, відкликаний або прострочений API token
                raise "API token required. Please contact api@alerts.in.ua for details."
            case 429:  # Перевищено ліміт запитів у хвилину
                raise "API Reach Limit. You should call API no more than 3-4 times per minute"

        data = response.json()

        if "message" in data:
            raise Exception(data["message"])

        _alerts = data["alerts"]
        _meta = data["meta"]

        self.locations = Locations(disclaimer="disclaimer", last_updated_at=_meta["last_updated_at"])

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
            self.locations.append(location)

        return self.locations


alerts = AlertsClient("04fb0e20d084953e768100bbcfec463b81b1191aab2203")  # 04fb0e20d084953e768100bbcfec463b81b1191aab2203
locations = alerts.get_active()
