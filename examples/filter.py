from pprint import pprint
from alerts.alerts_client import AlertsClient


alerts_client = AlertsClient("token")


def main():
    locations = alerts_client.get_active()

    """
    Перший спосіб використання фільтрів
    """

    air_raid = locations.filter(alert_type="air_raid")
    oblast = locations.filter(location_type="oblast")
    air_raid_and_oblast = locations.filter(alert_type="air_raid", location_type="oblast")

    pprint(air_raid)  # Місця лише з повітряною тревогою
    pprint(oblast)  # Лише області
    pprint(air_raid_and_oblast)  # Лише області з повітряною тревогою

    """
    Другий спосіб використання фільтрів
    """

    air_raid_filter = {"alert_type": "air_raid"}
    oblast_filter = {"location_type": "oblast"}
    air_raid_and_oblast_filter = {"alert_type": "air_raid", "location_type": "oblast"}

    air_raid = locations.filter(**air_raid_filter)
    oblast = locations.filter(**oblast_filter)
    air_raid_and_oblast = locations.filter(**air_raid_and_oblast_filter)

    pprint(air_raid)  # Місця лише з повітряною тревогою
    pprint(oblast)  # Лише області
    pprint(air_raid_and_oblast)  # Лише області з повітряною тревогою


if __name__ == "__main__":
    main()
