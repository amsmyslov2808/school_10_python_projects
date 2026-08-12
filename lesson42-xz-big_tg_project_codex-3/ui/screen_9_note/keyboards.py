import telebot


def get_screen_9_note_input_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Назад", callback_data="screen_9_back"
        )
    )
    return keyboard
