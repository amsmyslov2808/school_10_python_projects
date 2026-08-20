"""Сервисы экрана 4: поиск введённого пользователем города."""

from api.cities_api import find_city
from models.city import City


def get_city_by_name(city_name: str) -> City | None:
    """Находит введённый пользователем город через GeoNames."""

    return find_city(city_name)
