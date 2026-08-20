"""Сервисы экрана 2: подбор праздников для главного меню."""

from datetime import date, timedelta

from api.hollidays_api import get_holidays_from_api
from models.holliday import Holiday

# Для каждой из этих стран выполняется отдельный запрос к API праздников.
COUNTRY_CODES = ["RU", "US", "GB", "IN", "JP", "BR"]


def get_holidays_for_next_30_days() -> list[Holiday]:
    """Возвращает до пяти уникальных праздников ближайших 30 дней."""

    # Границы периода: сегодня и ещё 29 дней, то есть всего 30 дней.
    today = date.today()
    last_day = today + timedelta(days=29)
    all_holidays = []

    # Собираем праздники всех стран в один список.
    for country_code in COUNTRY_CODES:
        all_holidays.extend(get_holidays_from_api(country_code))

    # Здесь будут только подходящие праздники без повторов.
    holidays_for_next_30_days = []
    added_holidays = set()

    for holiday in all_holidays:
        if holiday.holiday_date < today or holiday.holiday_date > last_day:
            continue

        # Одинаковые название и дата означают, что праздник уже был добавлен.
        holiday_key = (holiday.name.lower(), holiday.holiday_date)
        if holiday_key in added_holidays:
            continue

        added_holidays.add(holiday_key)
        holidays_for_next_30_days.append(holiday)

    # Сначала показываем самый ближайший праздник.
    holidays_for_next_30_days.sort(key=lambda holiday: holiday.holiday_date)
    # Не перегружаем сообщение: выводим максимум пять праздников.
    return holidays_for_next_30_days[:5]
