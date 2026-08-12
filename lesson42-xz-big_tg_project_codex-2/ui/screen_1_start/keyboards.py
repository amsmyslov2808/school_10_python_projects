import telebot


def get_screen_2_main_menu_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Праздники на 7 дней", callback_data="screen_2_show_holidays"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Города куда съездить", callback_data="screen_2_input_city"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "История поездок", callback_data="screen_2_show_trips"
        )
    )
    return keyboard
