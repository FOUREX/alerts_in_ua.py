from abc import ABCMeta
from time import time

import aiohttp

from alerts_in_ua.base_alerts_client import BaseAlertsClient
from alerts_in_ua.exceptions import NotAuthorized, Forbidden, TooManyRequests


class AsyncAlertsClient(BaseAlertsClient, metaclass=ABCMeta):
    def __init__(self, token: str, requests_per_minute_limit: int = BaseAlertsClient.SOFT_LIMIT):
        """
        Клієнт. Дані беруться з сайту "alerts_in_ua.in.ua"

        :param token: Токен доступу
        :param requests_per_minute_limit: Ліміт запитів на хвилину
        """

        super().__init__(token, requests_per_minute_limit)

    async def _make_request(self, force: bool):
        async with aiohttp.ClientSession() as session:  # Шести поверховий пентхаус, лол
            async with session.get(url=self._url, headers=self._headers) as response:
                match response.status:
                    case 200:  # Ok
                        self._locations_json = await response.json()
                        self._headers["If-Modified-Since"] = response.headers["last-modified"]
                        self._response_status_code = 200
                    case 304:  # Не змінено
                        self._response_status_code = 304
                    case 401:  # Не авторизовано
                        raise NotAuthorized
                    case 403:  # Заборонено
                        raise Forbidden
                    case 429:  # Забагато запитів
                        raise TooManyRequests

    async def get_active_json(self, force: bool = False):
        if (time() - self._timer) > 60:
            self._timer = time()
            self._requests_per_minute = 0

        if self._requests_per_minute == BaseAlertsClient.HARD_LIMIT:
            return self._locations_json

        if self._requests_per_minute >= self._requests_per_minute_limit and not force:
            return self._locations_json

        self._requests_per_minute += 1

        await self._make_request(force)

        return self._locations_json

    async def get_active(self, force: bool = False):
        if (time() - self._timer) > 60:
            self._timer = time()
            self._requests_per_minute = 0

        if self._requests_per_minute == BaseAlertsClient.HARD_LIMIT:
            return self._locations

        if self._requests_per_minute >= self._requests_per_minute_limit and not force:
            return self._locations

        self._requests_per_minute += 1

        await self._make_request(force)
        self._make_locations()

        return self._locations
