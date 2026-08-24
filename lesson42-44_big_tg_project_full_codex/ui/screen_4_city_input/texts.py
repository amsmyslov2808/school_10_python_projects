"""Тексты результата поиска ближайших городов."""

from models.city import City


def get_screen_5_nearby_cities_text(cities: list[City]):
    """Формирует текст из списка городов, полученного от API."""

    output_text = "Ближайшие крупные города\n\n"

    for i in range(0, len(cities)):
        output_text += f"{i + 1}. {cities[i].name} — {cities[i].distance:.0f} км\n\n"

    return output_text
