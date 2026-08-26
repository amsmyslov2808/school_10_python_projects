"""Клавиатуры экранов выбора города и его подробностей."""

import telebot


def get_screen_5_nearby_cities_keyboard(
    count_nearby_cities: int,
) -> telebot.types.InlineKeyboardMarkup:
    """Создаёт по одной кнопке для каждого найденного города.

    Индекс записывается в ``callback_data`` с нуля и соответствует позиции
    объекта ``City`` в сохранённом в состоянии списке ``nearby_cities``.
    """

    keyboard = telebot.types.InlineKeyboardMarkup()

    # range не создаст кнопок, если API вернул пустой список.
    for city_index in range(0, count_nearby_cities):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_index+1}",
                callback_data=f"screen_5_choose_city_{city_index}",
            )
        )

    # Обработчик выбора города будет добавлен вместе с шестым экраном.
    return keyboard
