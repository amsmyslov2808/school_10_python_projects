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

    @classmethod
    def from_dictionary(cls, holiday_data: dict):
        # API возвращает словарь; здесь превращаем его в объект Holiday.
        return cls(
            country=holiday_data.get("country", "Неизвестная страна"),
            country_code=holiday_data.get("iso", ""),
            year=int(holiday_data.get("year", 0)),
            holiday_date=date.fromisoformat(holiday_data["date"]),
            day=holiday_data.get("day", ""),
            name=holiday_data.get("name", "Праздник без названия"),
            holiday_type=holiday_data.get("type", "HOLIDAY"),
        )

    def date_to_str(self):
        # Telegram удобнее показывать дату в привычном формате день.месяц.год.
        return self.holiday_date.strftime("%d.%m.%Y")

    def type_to_str(self):
        # Например, NATIONAL_HOLIDAY превращается в national holiday.
        return self.holiday_type.replace("_", " ").lower()
