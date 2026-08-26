"""Клавиатуры экранов, открываемых из главного меню."""

import telebot


def get_screen_3_holidays_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт кнопку возврата со страницы праздников в главное меню."""

    # Одинаковый callback_data позволит общему обработчику возврата открыть
    # главное меню, когда он будет добавлен в проект.
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_4_city_input_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт кнопку возврата с экрана ввода города."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_7_trips_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт кнопку возврата со страницы истории поездок."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    # Пять кнопок соответствуют пяти строкам демонстрационной истории.
    for city_number in range(1, 6):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_number}",
                callback_data=f"screen_7_choose_trip_{city_number}",
            )
        )

    # row размещает кнопки перелистывания рядом, в одной строке.
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
