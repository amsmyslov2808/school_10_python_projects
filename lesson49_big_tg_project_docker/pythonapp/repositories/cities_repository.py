"""Операции чтения и записи истории поездок в PostgreSQL."""

from datetime import datetime, date

from sqlalchemy import select

from models.visited_city import VisitedCity
from repositories.database import get_session


def insert_visited_city(tg_user_id: int, city_name: str):
    """Сохраняет выбранный город как новую поездку пользователя."""

    with get_session() as session:
        visited_city = VisitedCity(
            tg_user_id=tg_user_id,
            name=city_name,
            arrival_date=datetime.now().date(),
            note="Нет текста заметки",
        )
        session.add(visited_city)
        session.commit()


def select_all_visited_cities(tg_user_id: int) -> list[VisitedCity]:
    """Возвращает поездки пользователя от новых записей к старым."""

    with get_session() as session:
        query = (
            select(VisitedCity)
            .where(VisitedCity.tg_user_id == tg_user_id)
            .order_by(VisitedCity.arrival_date.desc())
        )
        return list(session.scalars(query))
