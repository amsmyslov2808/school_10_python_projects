MOCK_NEARBY_CITIES = [
    {"name": "Бердск", "distance": 37},
    {"name": "Искитим", "distance": 58},
    {"name": "Тогучин", "distance": 110},
    {"name": "Болотное", "distance": 126},
    {"name": "Томск", "distance": 265},
]


def get_screen_5_nearby_cities_text(cities: list[dict]):
    output_text = "Список городов\n\n"

    for city_number, city in enumerate(cities, start=1):
        output_text += (
            f"{city_number}. {city['name']} — {city['distance']} км\n\n"
        )

    return output_text.strip()
