from dataclasses import dataclass
from datetime import date


@dataclass
class Holiday:
    # Dataclass сам создаёт удобный конструктор для полей ниже.
    country: str
    country_code: str
    year: int
    holiday_date: date
    day: str
    name: str
    holiday_type: str

    def date_to_str(self):
        # Telegram удобнее показывать дату в привычном формате день.месяц.год.
        return self.holiday_date.strftime("%d.%m.%Y")

    def type_to_str(self):
        # Например, NATIONAL_HOLIDAY превращается в national holiday.
        return self.holiday_type.replace("_", " ").lower()
