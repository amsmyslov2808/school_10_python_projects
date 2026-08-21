"""Клавиатуры экранов, открываемых из главного меню."""

import telebot


def get_screen_3_holidays_keyboard():
    """Создаёт кнопку возврата из экрана праздников в главное меню."""

    # Inline-клавиатура отображается прямо под сообщением бота.
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            # callback_data — служебный идентификатор нажатия, не видимый пользователю.
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


def get_screen_7_trips_keyboard():
    """Создаёт кнопку возврата со страницы истории поездок."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    for city_number in range(1, 6):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_number}",
                callback_data=f"screen_7_choose_trip_{city_number}",
            )
        )

    keyboard.row(
        telebot.types.InlineKeyboardButton(
            "Назад", callback_data="screen_7_previous_page"
        ),
        telebot.types.InlineKeyboardButton(
            "Вперёд", callback_data="screen_7_next_page"
        ),
    )

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard
