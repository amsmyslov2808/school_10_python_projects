"""Бизнес-логика разделов главного меню приложения TravelHunter.

Модуль получает данные сразу для нескольких стран, выбирает события ближайшей
недели и готовит единый список для Telegram-интерфейса. HTTP-запросы при этом
остаются в API-слое, а обработчики не содержат бизнес-правил фильтрации.
Здесь же находится операция получения истории поездок из репозитория.
"""

from models.holiday import Holiday

from datetime import date, timedelta

from api.holidays_api import *

from repositories.cities_repository import *


def get_holidays_for_next_7_days() -> list[Holiday]:
    """Собирает до семи праздников трёх стран на ближайшую неделю.

    До итоговой сортировки списки объединяются по кругу: Россия, США, Китай.
    Такой алгоритм не позволяет одной стране сразу занять все семь позиций.
    """

    # Получаем отдельные списки праздников для каждой поддерживаемой страны.
    ru_holidays = get_holidays_from_api("RU")
    us_holidays = get_holidays_from_api("US")
    cn_holidays = get_holidays_from_api("CN")

    # Оставляем только праздники, которые наступят в ближайшие семь дней.
    ru_holidays = filter_holidays(ru_holidays)
    us_holidays = filter_holidays(us_holidays)
    cn_holidays = filter_holidays(cn_holidays)

    # Для каждого списка хранится отдельный индекс следующего ещё не взятого
    # праздника. Несколько присваиваний справа задают всем индексам значение 0.
    result_holidays_list = []
    ru_holidays_index = us_holidays_index = cn_holidays_index = 0
    is_run = True

    # По очереди берём по одному празднику из каждой страны, пока не наберём
    # семь праздников или пока не закончатся все три исходных списка.
    while is_run == True:
        # Цикл завершается, когда исчерпаны все источники либо набран лимит.
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
    """Оставляет праздники с датой в пределах семи дней, включая сегодня."""

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

    # Исходный порядок элементов сохраняется; общая сортировка выполняется
    # после объединения результатов разных стран.
    return filtered_holidays


def get_all_user_visited_cities(tg_user_id: int):
    """Получает из базы данных историю поездок пользователя."""

    return select_all_visited_cities(tg_user_id)
