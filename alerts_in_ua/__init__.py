__version__ = "1.3.3"

from alerts_in_ua.alerts_client import AlertsClient as AlertsClient
from alerts_in_ua.async_alerts_client import AsyncAlertsClient as AsyncAlertsClient
from alerts_in_ua.location import Location
from alerts_in_ua.locations import Locations
from alerts_in_ua.map_style import MapStyle

from alerts_in_ua.exceptions import (
    NotAuthorized as NotAuthorized,
    Forbidden as Forbidden,
    TooManyRequests as TooManyRequests,
    UnknownError as UnknownError
)

__all__: tuple[str] = (
    "__version__",
    "AlertsClient",
    "AsyncAlertsClient",
    "Location",
    "Locations",
    "MapStyle",
    "NotAuthorized",
    "Forbidden",
    "TooManyRequests",
    "UnknownError"
)
