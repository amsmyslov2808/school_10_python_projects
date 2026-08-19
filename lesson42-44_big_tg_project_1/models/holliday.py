from dataclasses import dataclass
from datetime import date


@dataclass
class Holiday:
    country: str
    holiday_date: date
    name: str

    def date_to_str(self):
        # Telegram удобнее показывать дату в привычном формате день.месяц.год.
        return self.holiday_date.strftime("%d.%m.%Y")
