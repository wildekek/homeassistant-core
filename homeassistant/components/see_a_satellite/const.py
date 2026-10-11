"""Constants for the See A Satellite Tonight integration."""

from datetime import timedelta
import logging
from typing import Final

DOMAIN: Final = "see_a_satellite"
LOGGER = logging.getLogger(__package__)

WEBSITE_URL: Final = "https://james.darpinian.com/satellites/"

CONF_CATALOG: Final = "catalog"
CONF_MAX_MAGNITUDE: Final = "max_magnitude"
CONF_CLOUD_COVER: Final = "cloud_cover"

# The website's own catalogs, and one built from CelesTrak and Quicksat.
CATALOG_BRIGHTEST: Final = "brightest"
CATALOG_STARLINK: Final = "starlink"
CATALOG_PUBLIC: Final = "public"
CATALOGS: Final = [CATALOG_BRIGHTEST, CATALOG_STARLINK, CATALOG_PUBLIC]

DEFAULT_MAX_MAGNITUDE: Final = 3.0

CATALOG_REFRESH: Final = timedelta(hours=12)
MAGNITUDES_REFRESH: Final = timedelta(days=7)
PREDICTION_REFRESH: Final = timedelta(hours=2)

ATTRIBUTION: Final = (
    "Predictions by See A Satellite Tonight (james.darpinian.com/satellites), "
    "orbital data from CelesTrak, cloud cover from Open-Meteo"
)
