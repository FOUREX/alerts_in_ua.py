__version__ = "1.1"

from alerts_in_ua.alerts_client import AlertsClient as AlertsClient
from alerts_in_ua.async_alerts_client import AsyncAlertsClient as AsyncAlertsClient
from alerts_in_ua.location import Location
from alerts_in_ua.locations import Locations

from alerts_in_ua.exceptions import (
    InvalidToken as InvalidToken,
    TooManyRequests as TooManyRequests,
    UnknownError as UnknownError
)

__all__: tuple[str] = (
    "AlertsClient",
    "AsyncAlertsClient",
    "Location",
    "Locations",
    "InvalidToken",
    "TooManyRequests",
    "UnknownError"
)
