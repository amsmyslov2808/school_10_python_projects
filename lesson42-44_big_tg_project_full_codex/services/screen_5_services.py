"""Сервисы экрана 5: ближайшие города и сохранение выбранной поездки."""

from api.geonames_api import find_nearby_cities
from models.city import City
from repositories.trips_repository import create_trip


def get_nearby_cities(city: City) -> list[City]:
    """Возвращает ближайшие города для экрана 5."""

    return find_nearby_cities(city)


def save_trip(tg_user_id: int, city_name: str):
    """Сохраняет выбранный пользователем город как новую поездку."""

    return create_trip(tg_user_id, city_name)
