from datetime import datetime

from sqlalchemy import select

from models.visited_city import VisitedCity
from repositories.database import Session


def create_trip(tg_user_id: int, city_name: str) -> VisitedCity:
    """Сохраняет выбранный город как новую поездку пользователя."""

    with Session() as session:
        trip = VisitedCity(
            tg_user_id=tg_user_id,
            name=city_name,
            arrival_date=datetime.now(),
            note=None,
        )
        session.add(trip)
        session.commit()
        session.refresh(trip)
        return trip


def get_trips(tg_user_id: int) -> list[VisitedCity]:
    """Возвращает поездки пользователя: новые записи идут первыми."""

    with Session() as session:
        query = (
            select(VisitedCity)
            .where(VisitedCity.tg_user_id == tg_user_id)
            .order_by(VisitedCity.arrival_date.desc())
        )
        return list(session.scalars(query))


def get_trip(trip_id: int, tg_user_id: int) -> VisitedCity | None:
    """Возвращает одну поездку, но только владельцу с указанным Telegram ID."""

    with Session() as session:
        query = select(VisitedCity).where(
            VisitedCity.id == trip_id, VisitedCity.tg_user_id == tg_user_id
        )
        return session.scalar(query)


def update_trip_note(trip_id: int, tg_user_id: int, note: str):
    """Сохраняет заметку к поездке и возвращает True при успехе."""

    with Session() as session:
        trip = session.scalar(
            select(VisitedCity).where(
                VisitedCity.id == trip_id, VisitedCity.tg_user_id == tg_user_id
            )
        )
        if trip is None:
            return False

        trip.note = note
        session.commit()
        return True
