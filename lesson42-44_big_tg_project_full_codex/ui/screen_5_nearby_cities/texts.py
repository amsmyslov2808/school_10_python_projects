from models.city import City


def get_screen_5_nearby_cities_text(cities: list[City]):
    """Формирует список ближайших городов с расстояниями."""

    output_text = "Ближайшие города\n\n"
    for city_number, city in enumerate(cities, start=1):
        output_text += f"{city_number}. {city.name} — {city.distance:.0f} км\n\n"
    return output_text.strip()
