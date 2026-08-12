from datetime import date, timedelta

from api.hollidays_api import get_holidays_from_api
from models.holliday import Holiday


COUNTRY_CODES = ["RU", "US", "GB", "IN", "JP", "BR"]


def get_holidays_for_next_30_days() -> list[Holiday]:
    today = date.today()
    last_day = today + timedelta(days=29)
    all_holidays = []

    for country_code in COUNTRY_CODES:
        country_holidays = get_holidays_from_api(country_code)
        all_holidays.extend(country_holidays)

    holidays_for_next_30_days = []
    added_holidays = set()

    for holiday in all_holidays:
        if holiday.holiday_date < today or holiday.holiday_date > last_day:
            continue

        holiday_key = (
            holiday.name.lower(),
            holiday.holiday_date,
        )

        if holiday_key in added_holidays:
            continue

        added_holidays.add(holiday_key)
        holidays_for_next_30_days.append(holiday)

    holidays_for_next_30_days.sort(
        key=lambda holiday: holiday.holiday_date
    )

    return holidays_for_next_30_days[:5]
