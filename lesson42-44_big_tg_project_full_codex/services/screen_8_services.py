"""Сервисы экрана 8: получение подробностей выбранной поездки."""

from repositories.trips_repository import get_trip


def get_user_trip(trip_id: int, tg_user_id: int):
    """Получает одну поездку пользователя."""

    return get_trip(trip_id, tg_user_id)
