from datetime import date, timedelta

from api.hollidays_api import get_holidays_from_api
from models.holliday import Holiday

from api.cities_api import find_city, find_nearby_cities, get_city_info
from models.city import City
from repositories.cities_repository import create_trip, get_trip, get_trips, update_trip_note

# Берём праздники нескольких регионов мира, как в проекте для урока.
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


def get_city_by_name(city_name: str) -> City | None:
    """Находит введённый пользователем город через GeoNames."""

    return find_city(city_name)


def get_nearby_cities(city: City) -> list[City]:
    """Возвращает ближайшие города для экрана 5."""

    return find_nearby_cities(city)


def get_selected_city_info(city_name: str) -> tuple[str, str | None]:
    """Возвращает описание и изображение выбранного города."""

    return get_city_info(city_name)


def save_trip(tg_user_id: int, city_name: str):
    """Сохраняет поездку в базе данных."""

    return create_trip(tg_user_id, city_name)


def get_user_trips(tg_user_id: int):
    """Получает историю поездок пользователя."""

    return get_trips(tg_user_id)


def get_user_trip(trip_id: int, tg_user_id: int):
    """Получает одну поездку пользователя."""

    return get_trip(trip_id, tg_user_id)


def save_trip_note(trip_id: int, tg_user_id: int, note: str):
    """Сохраняет заметку к поездке."""

    return update_trip_note(trip_id, tg_user_id, note)
