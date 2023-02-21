class MapStyle:
    def __init__(self,
                 no_data: str = "#1a2636",
                 air_raid: str = "#762b2d",
                 artillery_shelling: str = "#ff7b00",
                 urban_fights: str = "#4e3cb4",
                 chemical: str = "#b7ea35",
                 nuclear: str = "#000",
                 stroke_width: str = ".7",
                 stroke_color: str = "#ffffff",
                 background_color: str = "#14181D",
                 dpi: int = 72):
        """
        Стиль карти для її генерації

        :param no_data: Кольор області без тревоги
        :param air_raid: Колір області з повітряною тревогою
        :param artillery_shelling: Колір області з загрозою артобстрілу
        :param urban_fights: Колір області з загрозою вуличних боїв
        :param chemical: Колір області з хімічною загрозою
        :param nuclear: Колір області з радіаційною загрозою
        :param stroke_width: Товщина контурів областей
        :param stroke_color: Колір контурів областей
        :param background_color: Колір фону
        :param dpi: Кількість точок на дюйм (чим більше значення - тим більше зображення на виході)
        """

        self.no_data = no_data
        self.air_raid = air_raid
        self.artillery_shelling = artillery_shelling
        self.urban_fights = urban_fights
        self.chemical = chemical
        self.nuclear = nuclear
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color
        self.background_color = background_color
        self.dpi = dpi

    def __repr__(self):
        return f"MapStyle(no_data: {self.no_data}, air_raid: {self.air_raid}, " \
               f"artillery_shelling: {self.artillery_shelling}, urban_fights: {self.urban_fights}, " \
               f"chemical: {self.chemical}, nuclear: {self.nuclear}, stroke_width: {self.stroke_width}, " \
               f"stroke_color: {self.stroke_color}, background_color: {self.background_color}, dpi: {self.dpi})"
