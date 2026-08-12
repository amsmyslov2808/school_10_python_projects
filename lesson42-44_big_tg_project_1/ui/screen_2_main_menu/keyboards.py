import telebot


def get_screen_3_holidays_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_4_city_input_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_7_trips_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard
