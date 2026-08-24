import telebot


def get_screen_8_trip_info_keyboard():
    """Создаёт кнопки действий с выбранной поездкой."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Написать заметку", callback_data="screen_8_write_note"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton("Назад", callback_data="screen_8_back")
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_8_main_menu"
        )
    )
    return keyboard
