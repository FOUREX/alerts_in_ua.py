from alerts.location import Location


class Locations(list):
    """
    Список для місць з тревогою для більш зручної маніпуляції над ними
    """

    def __init__(self, *__locations: Location, disclaimer: str, last_updated_at: str):
        super(Locations, self).__init__(__locations)

        self.disclaimer = disclaimer
        self.last_updated_at = last_updated_at
        self.type = "full"  # Ну потому что v1

    def append(self, __location: Location) -> None:
        super(Locations, self).append(__location)

    def filter(self, **filters) -> list[Location]:
        """
        Повертає список місць які підпадають під вказані фільтри

        :param filters: Фільтри
        """

        def location_filter(location: Location):
            for _filter in filters:
                if getattr(location, _filter) != filters[_filter]:
                    return False
            return True

        return list(filter(location_filter, self))
