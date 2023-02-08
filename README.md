# Alerts_in_ua.py

Бібліотека для користування API сайту "alerts.in.ua".
**Бібліотека досі в розробці, якщо ви знайшли помилку,
звертайтеся до розробника!** Telegram: [@FOUREX_dot_py](https://t.me/FOUREX_dot_py)

## Приклад використання:
```python
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
```

## Приклад використання асинхронного клієнта:
Рекомендовано використовувати для ботів.
```python
import asyncio

from alerts.async_alerts_client import AsyncAlertsClient


alerts_client = AsyncAlertsClient("token")  # Ініціалізуємо клієнт


async def main():
    locations = await alerts_client.get_active()  # Отримуємо список місць з тревогою

    # Фільтруємо список місць залишаючи місця з ПОВІТРЯНОЮ тревогою
    air_raid_locations = locations.filter(alert_type="air_raid")

    for location in air_raid_locations:
        # Виводимо назву та час початку тревоги кожного місця зі списку
        print(location.location_title, location.started_at)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
```