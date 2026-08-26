"""Бизнес-операции экранов ввода города и просмотра ближайших городов.

Сейчас функции являются тонкими обёртками над GeoNames API. Отдельный слой всё
равно полезен: обработчики зависят от понятных операций приложения, а позднее
сюда можно добавить кеширование, дополнительные фильтры или работу с БД.
"""

from api.geonames_api import *
from models.city import City


def get_city_by_name(city_name: str) -> City | None:
    """Находит введённый пользователем город либо возвращает ``None``."""

    return find_city_by_name(city_name)


def get_nearby_cities(city: City) -> list[City]:
    """Возвращает подготовленный API список ближайших крупных городов."""

    return find_nearby_cities(city)
