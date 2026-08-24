import telebot


def get_screen_6_city_info_keyboard():
    """Создаёт кнопку возврата в главное меню."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_6_main_menu"
        )
    )
    return keyboard
