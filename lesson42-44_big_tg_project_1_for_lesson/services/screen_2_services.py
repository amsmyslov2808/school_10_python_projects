"""Сервисы экрана 2: подбор праздников для главного меню."""

from datetime import date, timedelta

from api.hollidays_api import get_holidays_from_api
from models.holliday import Holiday

# Для каждой из этих стран выполняется отдельный запрос к API праздников.
COUNTRY_CODES = ["RU", "US", "GB", "IN", "JP", "BR"]
MAX_HOLIDAYS = 7


def get_holidays_for_next_7_days() -> list[Holiday]:
    """Возвращает до семи праздников ближайшей недели с чередованием стран."""

    # Границы периода: сегодня и ещё шесть дней, то есть всего семь дней.
    today = date.today()
    last_day = today + timedelta(days=6)
    holidays_by_country = {}

    # Для каждой страны оставляем только праздники ближайшей недели и убираем
    # возможные повторы в ответе API.
    for country_code in COUNTRY_CODES:
        added_holidays = set()
        country_holidays = []
        for holiday in get_holidays_from_api(country_code):
            if holiday.holiday_date < today or holiday.holiday_date > last_day:
                continue

            holiday_key = (holiday.name.lower(), holiday.holiday_date)
            if holiday_key in added_holidays:
                continue

            added_holidays.add(holiday_key)
            country_holidays.append(holiday)

        # Внутри одной страны сначала показываем ближайшие праздники.
        holidays_by_country[country_code] = sorted(
            country_holidays, key=lambda holiday: holiday.holiday_date
        )

    result = []
    round_number = 0
    while len(result) < MAX_HOLIDAYS:
        added_on_this_round = False

        # За один круг берём не более одного праздника от каждой страны.
        # На следующем круге можно взять её второй праздник, если он есть.
        for country_code in COUNTRY_CODES:
            country_holidays = holidays_by_country[country_code]
            if round_number >= len(country_holidays):
                continue

            result.append(country_holidays[round_number])
            added_on_this_round = True
            if len(result) == MAX_HOLIDAYS:
                return result

        # Во всех странах закончились подходящие праздники.
        if not added_on_this_round:
            break
        round_number += 1

    return result
