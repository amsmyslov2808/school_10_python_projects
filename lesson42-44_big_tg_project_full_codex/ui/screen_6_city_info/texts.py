def get_screen_6_city_info_text(city_name: str, description: str):
    """Формирует текст экрана с информацией о городе."""

    if description == "":
        description = "К сожалению, краткое описание города не найдено."

    return f"{city_name}\n\n{description}"
