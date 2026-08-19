from datetime import date

import requests

from models.holliday import Holiday

API_NINJAS_KEY = "PI4IXDuJugrwuAWLKo2c8yZYOHTQqt11yebJ38Df"
API_NINJAS_HOLIDAYS_URL = "https://api.api-ninjas.com/v2/holidays"


def get_holidays_from_api(country_code: str) -> list[Holiday]:
    response = requests.get(
        API_NINJAS_HOLIDAYS_URL,
        params={"country": country_code},
        headers={"X-Api-Key": API_NINJAS_KEY},
        timeout=10,
    )

    response.raise_for_status()

    holidays_data = response.json()

    output_holidays = []

    for current_holiday in holidays_data:
        output_holidays.append(
            Holiday(
                country=current_holiday["country"],
                name=current_holiday["name"],
                holiday_date=date.fromisoformat(current_holiday["date"]),
            )
        )

    return output_holidays
