"""Получение официальных праздников через API Ninjas."""

from datetime import date

import requests

from models.holliday import Holiday

# Ключ авторизует запросы к внешнему API. В рабочем приложении его следует
# хранить в переменной окружения, а не в исходном коде.
API_NINJAS_KEY = "PI4IXDuJugrwuAWLKo2c8yZYOHTQqt11yebJ38Df"
API_NINJAS_HOLIDAYS_URL = "https://api.api-ninjas.com/v2/holidays"


def get_holidays_from_api(country_code: str) -> list[Holiday]:
    """Запрашивает праздники страны и преобразует ответ API в модели Holiday."""

    # Параметр country задаёт страну в формате ISO 3166-1 alpha-2, например RU.
    # timeout не позволяет боту надолго зависнуть при проблемах с сетью.
    response = requests.get(
        API_NINJAS_HOLIDAYS_URL,
        params={"country": country_code},
        headers={"X-Api-Key": API_NINJAS_KEY},
        timeout=10,
    )

    # Превращаем HTTP-ошибки API в исключение вместо обработки неверного ответа.
    response.raise_for_status()

    # API возвращает список словарей; каждому словарю соответствует один праздник.
    holidays_data = response.json()
    output_holidays = []

    for current_holiday in holidays_data:
        # Преобразуем строку даты формата YYYY-MM-DD в объект date модели.
        output_holidays.append(
            Holiday(
                country=current_holiday["country"],
                name=current_holiday["name"],
                holiday_date=date.fromisoformat(current_holiday["date"]),
            )
        )

    return output_holidays
