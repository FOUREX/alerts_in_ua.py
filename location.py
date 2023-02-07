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