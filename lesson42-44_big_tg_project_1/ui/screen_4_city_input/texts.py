"""Тексты результата поиска ближайших городов."""

from models.city import City


def get_screen_5_nearby_cities_text(
    start_city: City, nearby_cities: list[City]
) -> str:
    """Формирует нумерованный список найденных городов и расстояний до них."""

    # Имя исходного города берётся из ответа GeoNames, поэтому его написание
    # может отличаться от пользовательского ввода регистром или формой.
    output_text = f"Список городов куда можно съездить из города {start_city.name}\n\n"

    # Отдельный счётчик нужен для понятной человеку нумерации с единицы.
    city_number = 0
    for nearby_city in nearby_cities:
        city_number += 1
        # :.0f округляет расстояние до целых километров только при отображении;
        # точное значение остаётся сохранено внутри объекта City.
        output_text += (
            f"{city_number}. {nearby_city.name} — {nearby_city.distance:.0f} км\n\n"
        )

    return output_text
