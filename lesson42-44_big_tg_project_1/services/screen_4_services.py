"""Сервисы экрана 4: поиск введённого пользователем города."""

from api.geonames_api import *
from models.city import City


def get_city_by_name(city_name: str) -> City | None:
    """Находит введённый пользователем город через GeoNames."""

    return find_city_by_name(city_name)


def get_nearby_cities(city: City) -> list[City]:
    """Возвращает ближайшие города для экрана 5."""

    return find_nearby_cities(city)
