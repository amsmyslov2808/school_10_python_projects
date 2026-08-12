import telebot


def get_screen_3_holidays_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_3_main_menu"
        )
    )
    return keyboard
