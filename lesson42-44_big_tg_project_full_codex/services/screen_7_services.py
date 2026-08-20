"""Сервисы экрана 7: получение истории поездок пользователя."""

from repositories.trips_repository import get_trips


def get_user_trips(tg_user_id: int):
    """Получает историю поездок пользователя."""

    return get_trips(tg_user_id)
