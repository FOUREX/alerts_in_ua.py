__version__ = "1.0"

from alerts.alerts_client import AlertsClient as AlertsClient
from alerts.async_alerts_client import AsyncAlertsClient as AsyncAlertsClient
from alerts.location import Location
from alerts.locations import Locations

from alerts.exceptions import (
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
