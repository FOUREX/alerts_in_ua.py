class Active:
    def __init__(self, name: str, place_type: str, started_at: ...):
        self.name = name
        self.place_type = place_type
        self.started_at = started_at

    def __repr__(self):
        return f"name: {self.name}, type: {self.place_type}, started_at: {self.started_at}"


class Client:
    def __init__(self, token: str):
        self.token = token

    async def get_active(self) -> list[Active | None]:
        ...

    async def is_active(self, name: str):
        ...
