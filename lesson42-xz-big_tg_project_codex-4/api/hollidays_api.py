import requests

from models.holliday import Holiday

API_NINJAS_KEY = "PI4IXDuJugrwuAWLKo2c8yZYOHTQqt11yebJ38Df"
API_NINJAS_HOLIDAYS_URL = "https://api.api-ninjas.com/v2/holidays"


def get_holidays_from_api(country_code: str) -> list[Holiday]:
    if API_NINJAS_KEY.startswith("ВСТАВЬТЕ_СЮДА"):
        raise ValueError("Вставьте ключ API Ninjas в api/hollidays_api.py")

    response = requests.get(
        API_NINJAS_HOLIDAYS_URL,
        params={"country": country_code},
        headers={"X-Api-Key": API_NINJAS_KEY},
        timeout=10,
    )
    response.raise_for_status()

    holidays_data = response.json()

    if isinstance(holidays_data, list) == False:
        raise ValueError("API Ninjas вернул неизвестный ответ")

    holidays = []

    for holiday_data in holidays_data:
        holidays.append(Holiday.from_dictionary(holiday_data))

    return holidays
