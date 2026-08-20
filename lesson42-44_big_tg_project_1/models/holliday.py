"""Модель праздника, получаемого из внешнего API."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Holiday:
    """Хранит сведения об одном празднике в выбранной стране."""

    country: str
    holiday_date: date
    name: str

    def date_to_str(self) -> str:
        """Возвращает дату в формате, удобном для сообщения Telegram."""

        # Telegram удобнее показывать дату в привычном формате день.месяц.год.
        return self.holiday_date.strftime("%d.%m.%Y")
