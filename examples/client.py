from alerts.alerts_client import AlertsClient  # Імпортуємо клієнт


alerts_client = AlertsClient("token")  # Ініціалізуємо клієнт


def main():
    locations = alerts_client.get_active()  # Отримуємо список місць з тревогою

    # Фільтруємо список місць залишаючи місця з ПОВІТРЯНОЮ тревогою
    air_raid_locations = locations.filter(alert_type="air_raid")

    for location in air_raid_locations:
        # Виводимо назву та час початку тревоги кожного місця зі списку
        print(location.location_title, location.started_at)


if __name__ == "__main__":
    main()
