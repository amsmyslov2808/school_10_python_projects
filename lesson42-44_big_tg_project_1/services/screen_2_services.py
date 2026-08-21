"""Бизнес-логика приложения TravelHunter (заготовка).

Сервисы должны связывать UI, внешние API и репозитории: например, получать
координаты введённого города, подбирать ближайшие города и сохранять поездку.
Так обработчики Telegram останутся короткими и будут отвечать только за диалог.
"""

from models.holliday import Holiday

from datetime import date, timedelta

from api.hollidays_api import *


def get_holidays_for_next_7_days() -> list[Holiday]:
    # Получаем отдельные списки праздников для каждой поддерживаемой страны.
    ru_holidays = get_holidays_from_api("RU")
    us_holidays = get_holidays_from_api("US")
    cn_holidays = get_holidays_from_api("CN")

    # Оставляем только праздники, которые наступят в ближайшие семь дней.
    ru_holidays = filter_holidays(ru_holidays)
    us_holidays = filter_holidays(us_holidays)
    cn_holidays = filter_holidays(cn_holidays)

    result_holidays_list = []
    ru_holidays_index = us_holidays_index = cn_holidays_index = 0
    is_run = True

    # По очереди берём по одному празднику из каждой страны, пока не наберём
    # семь праздников или пока не закончатся все три исходных списка.
    while is_run == True:
        if (
            ru_holidays_index == len(ru_holidays)
            and us_holidays_index == len(us_holidays)
            and cn_holidays_index == len(cn_holidays)
        ) or len(result_holidays_list) == 7:
            is_run = False

        if ru_holidays_index < len(ru_holidays) and len(result_holidays_list) < 7:
            result_holidays_list.append(ru_holidays[ru_holidays_index])
            ru_holidays_index += 1

        if us_holidays_index < len(us_holidays) and len(result_holidays_list) < 7:
            result_holidays_list.append(us_holidays[us_holidays_index])
            us_holidays_index += 1

        if cn_holidays_index < len(cn_holidays) and len(result_holidays_list) < 7:
            result_holidays_list.append(cn_holidays[cn_holidays_index])
            cn_holidays_index += 1

    # После объединения располагаем праздники в хронологическом порядке.
    result_holidays_list = sorted(
        result_holidays_list, key=lambda holiday: holiday.holiday_date
    )

    return result_holidays_list


def filter_holidays(holidays: list[Holiday]) -> list[Holiday]:
    # Границы периода включаются в выборку: от сегодняшнего дня до шестого
    # дня после него, то есть всего семь календарных дней.
    today = date.today()
    last_day = today + timedelta(days=6)

    filtered_holidays = []

    # Проверяем дату каждого праздника и сохраняем подходящие элементы.
    for current_holiday in holidays:
        if (
            current_holiday.holiday_date >= today
            and current_holiday.holiday_date <= last_day
        ):
            filtered_holidays.append(current_holiday)

    return filtered_holidays
