from typing import TypeVar

from alerts_in_ua.location import Location


Self = TypeVar("Self")


class Locations(list):
    """
    Список для місць з тревогою для більш зручної маніпуляції над ними
    """

    def __init__(self, *__locations: Location, disclaimer: str, last_updated_at: str):
        super(Locations, self).__init__(__locations)

        self.disclaimer = disclaimer
        self.last_updated_at = last_updated_at
        self.type = "full"  # Ну тому що v1

    def __getattr__(self, item) -> list:
        return [getattr(location, item) for location in self]

    def append(self, __location: Location) -> None:
        super(Locations, self).append(__location)

    def remove(self, __location: Location) -> None:
        super(Locations, self).remove(__location)

    def filter(self, **filters) -> Self:
        """
        Повертає список місць які підпадають під вказані фільтри

        :param filters: Фільтри
        """

        def location_filter(location: Location) -> bool:
            for filter_name in filters:
                if getattr(location, filter_name) != filters[filter_name]:
                    return False
            return True

        return Locations(
            *list(filter(location_filter, self)),
            disclaimer=self.disclaimer,
            last_updated_at=self.last_updated_at
        )
