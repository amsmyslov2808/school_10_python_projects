"""SQLAlchemy-модель сохранённой пользователем поездки."""

from datetime import date

from sqlalchemy import BigInteger, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from repositories.database import Base


class VisitedCity(Base):
    """Описывает один выбранный пользователем город в таблице поездок.

    Идентификатор пользователя Telegram связывает запись с его личной историей,
    а дата прибытия и заметка содержат сведения о поездке.
    """

    __tablename__ = "visited_cities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    arrival_date: Mapped[date] = mapped_column(Date, nullable=False)
    note: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    def arrival_date_to_normal_str(self) -> str:
        """Возвращает дату прибытия в привычном формате ``дд.мм.гггг``."""

        return self.arrival_date.strftime("%d.%m.%Y")
