import requests

from models.holliday import Holiday

# Ключ API Ninjas используется в заголовке каждого запроса.
API_NINJAS_KEY = "PI4IXDuJugrwuAWLKo2c8yZYOHTQqt11yebJ38Df"
API_NINJAS_HOLIDAYS_URL = "https://api.api-ninjas.com/v2/holidays"


def get_holidays_from_api(country_code: str) -> list[Holiday]:
    """Запрашивает праздники указанной страны у API Ninjas."""

    # Передаём код страны как параметр запроса, а ключ — в HTTP-заголовке.
    response = requests.get(
        API_NINJAS_HOLIDAYS_URL,
        params={"country": country_code},
        headers={"X-Api-Key": API_NINJAS_KEY},
        timeout=10,
    )
    # При статусе 4xx или 5xx метод выбросит RequestException.
    response.raise_for_status()
    # Преобразуем JSON-ответ API в обычные Python-данные.
    holidays_data = response.json()

    if not isinstance(holidays_data, list):
        raise ValueError("API Ninjas вернул неизвестный ответ")

    # Каждый словарь API преобразуем в объект нашей модели Holiday.
    return [Holiday.from_dictionary(holiday_data) for holiday_data in holidays_data]
