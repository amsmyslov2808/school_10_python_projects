import telebot


def get_screen_6_city_info_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Вернуться в меню", callback_data="screen_6_main_menu"
        )
    )
    return keyboard
