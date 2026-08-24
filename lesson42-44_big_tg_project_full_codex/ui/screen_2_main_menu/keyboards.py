"""Клавиатуры экранов, открываемых из главного меню."""

import telebot


def get_screen_3_holidays_keyboard():
    """Создаёт кнопку возврата со страницы праздников в главное меню."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_3_main_menu"
        )
    )
    return keyboard


def get_screen_4_city_input_keyboard():
    """Создаёт кнопку возврата с экрана ввода города."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_7_trips_keyboard(
    trips_count: int, page: int, has_next_page: bool
):
    """Создаёт кнопки выбора поездок и переключения страниц."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    for city_number in range(1, trips_count + 1):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_number}",
                callback_data=f"screen_7_choose_trip_{city_number}",
            )
        )

    if page > 0:
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                "Назад", callback_data="screen_7_previous_page"
            )
        )

    if has_next_page:
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                "Вперёд", callback_data="screen_7_next_page"
            )
        )

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_7_main_menu"
        ),
    )
    return keyboard
