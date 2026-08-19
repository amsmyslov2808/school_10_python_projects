from dataclasses import dataclass


@dataclass
class City:
    """Город, полученный из GeoNames."""

    name: str
    latitude: float
    longitude: float
    country: str = ""
    distance: float = 0
