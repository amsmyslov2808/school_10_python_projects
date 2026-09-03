"""Бизнес-операции экрана выбора ближайшего города."""

from repositories.cities_repository import *


def save_visited_city(tg_user_id: int, city_name: str):
    """Сохраняет выбранный пользователем город как новую поездку."""

    insert_visited_city(tg_user_id, city_name)
