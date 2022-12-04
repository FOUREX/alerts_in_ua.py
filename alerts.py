import requests


class Location:
    def __init__(self,
                 location_id: int,
                 location_title: str,
                 location_type: str,
                 started_at: str,
                 finished_at: str,
                 updated_at: str,
                 alert_type: str,
                 location_uid: str,
                 location_oblast: str,
                 location_raion: str | None,
                 notes: str,
                 calculated: bool):
        self.id = location_id
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
               f"location_oblast: {self.location_oblast}, location_raion: {self.location_raion}, notes: {self.notes}, "\
               f"calculated: {self.calculated})"


class Client:
    def __init__(self, token: str):
        self.token = token

    def get_active(self) -> list[Location]:
        response = requests.get(f"https://dev-api.alerts.in.ua/v1/alerts/active.json?token={self.token}")

        match response.status_code:
            case 200:
                data = response.json()
                alerts = data["alerts"]
                active = []

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
                    location_raion = alert["location_raion"]
                    notes = alert["notes"]
                    calculated = alert["calculated"]

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
                        calculated
                    )

                    active.append(location)

                return active
            case 304:
                ...
            case 401, 429:
                message = response.json()["message"]
                raise message
