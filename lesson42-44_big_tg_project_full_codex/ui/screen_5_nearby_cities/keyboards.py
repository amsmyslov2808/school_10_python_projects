import telebot


def get_screen_5_nearby_cities_keyboard(cities_count: int):
    """Создаёт кнопки только для городов, которые нашлись в API."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    for city_number in range(1, cities_count + 1):
        keyboard.add(telebot.types.InlineKeyboardButton(
            f"Выбрать город {city_number}",
            callback_data=f"screen_5_choose_city_{city_number}",
        ))
    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="screen_5_back"))
    return keyboard
