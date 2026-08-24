from datetime import date

import requests

from models.holliday import Holiday

# Ключ API Ninjas используется в заголовке каждого запроса.
API_NINJAS_KEY = "PI4IXDuJugrwuAWLKo2c8yZYOHTQqt11yebJ38Df"
API_NINJAS_HOLIDAYS_URL = "https://api.api-ninjas.com/v2/holidays"


def get_holidays_from_api(country_code: str) -> list[Holiday]:
    """Запрашивает праздники указанной страны у API Ninjas."""

    # Отправляем в API код страны и ключ доступа.
    response = requests.get(
        API_NINJAS_HOLIDAYS_URL,
        params={"country": country_code},
        headers={"X-Api-Key": API_NINJAS_KEY},
        timeout=10,
    )

    # Если API вернул ошибку, программа создаст исключение.
    response.raise_for_status()

    # API возвращает список словарей с праздниками.
    holidays_data = response.json()
    output_holidays = []

    for current_holiday in holidays_data:
        # Превращаем каждый словарь API в объект Holiday.
        output_holidays.append(
            Holiday(
                country=current_holiday["country"],
                country_code=current_holiday["iso"],
                year=int(current_holiday["year"]),
                holiday_date=date.fromisoformat(current_holiday["date"]),
                day=current_holiday["day"],
                name=current_holiday["name"],
                holiday_type=current_holiday["type"],
            )
        )

    return output_holidays
