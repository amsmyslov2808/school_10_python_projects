"""Клавиатуры экранов, открываемых из главного меню."""

import telebot


def get_screen_3_holidays_keyboard():
    """Создаёт кнопку возврата со страницы праздников в главное меню."""

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
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

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard
