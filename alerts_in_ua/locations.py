from xml.etree import ElementTree
from typing import TypeVar
from io import BytesIO

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

from alerts_in_ua.location import Location
from alerts_in_ua.map_style import MapStyle


DIRECTORY = "/".join(__file__.replace('\\', '/').split('/')[:-1])

Self = TypeVar("Self")


class Locations(list):
    """
    Список для місць з тривогою для більш зручної маніпуляції над ними
    """

    def __init__(self, *__locations: Location, disclaimer: str, last_updated_at: str) -> None:
        super(Locations, self).__init__(__locations)

        self.disclaimer = disclaimer
        self.last_updated_at = last_updated_at
        self.type = "full"  # Ну тому що v1

    def __getattr__(self, item) -> list:
        return [getattr(location, item) for location in self]

    def __contains__(self, item: str | int) -> bool:
        if isinstance(item, int):
            return item in self.location_uid
        else:
            return item in self.location_title

    def append(self, __location: Location) -> None:
        super(Locations, self).append(__location)

    def remove(self, __location: Location) -> None:
        super(Locations, self).remove(__location)

    def __build_map(self, map_style: MapStyle) -> BytesIO:
        svg_ukraine_map = BytesIO()

        with open(f"{DIRECTORY}/resources/map/Ukraine simple.svg", "r", encoding="utf-8") as file:
            svg_ukraine_map.write(bytes(file.read(), "utf-8"))
            svg_ukraine_map.seek(0)

        ukraine_map = ElementTree.parse(svg_ukraine_map)
        ukraine_map_root = ukraine_map.getroot()

        ukraine_map_root.set("stroke", map_style.stroke_color)
        ukraine_map_root.set("stroke_width", map_style.stroke_width)

        for children in ukraine_map_root:
            location_uid = children.attrib["location_uid"]

            if location_uid in self.location_uid:
                location = self.get_location(location_uid)
                children.set("fill", getattr(map_style, location.alert_type))
            else:
                children.set("fill", map_style.no_data)

        svg_ukraine_map.truncate(0)
        svg_ukraine_map.seek(0)
        ukraine_map.write(svg_ukraine_map)
        svg_ukraine_map.seek(0)

        return svg_ukraine_map

    def get_location(self, item: str | int) -> Location | None:
        """
        Повертає місце за його UID (location_uid) або назвою (location_title)

        :param item: UID (location_uid) або назва місця (location_title)
        """

        if isinstance(item, int) or item.isnumeric():
            attr = "location_uid"
        else:
            attr = "location_title"

        for location in self:
            if getattr(location, attr) == item:
                return location

        return None

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

    def render_map(self, map_style: MapStyle = MapStyle()) -> BytesIO:
        """
        Рендер карти тривог в .png форматі
        """

        svg_ukraine_map = self.__build_map(map_style)
        alerts_map = BytesIO()

        alerts_map.write(
            renderPM.drawToString(
                svg2rlg(svg_ukraine_map),
                fmt="PNG",
                bg=int(map_style.background_color[1:], 16),
                dpi=map_style.dpi
            )
        )
        alerts_map.seek(0)

        return alerts_map
