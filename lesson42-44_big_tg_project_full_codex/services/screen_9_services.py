"""Сервисы экрана 9: сохранение заметки к поездке."""

from repositories.trips_repository import update_trip_note


def save_trip_note(trip_id: int, tg_user_id: int, note: str):
    """Сохраняет заметку к поездке."""

    return update_trip_note(trip_id, tg_user_id, note)
