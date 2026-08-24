"""Клавиатуры экранов выбора города и его подробностей."""

import telebot


def get_screen_5_nearby_cities_keyboard(count_nearby_cities):
    """Создаёт кнопки выбора города из списка и возврата к вводу."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    for city_index in range(0, count_nearby_cities):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_index+1}",
                callback_data=f"screen_5_choose_city_{city_index}",
            )
        )

    return keyboard
