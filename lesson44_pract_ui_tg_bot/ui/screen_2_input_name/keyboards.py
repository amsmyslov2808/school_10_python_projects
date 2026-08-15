import telebot


def get_inline_keyboard_for_screen_3_choose_gender():
    # Создаём клавиатуру с кнопками под сообщением.
    keyboard = telebot.types.InlineKeyboardMarkup()
    # callback_data — данные, которые бот получит после нажатия кнопки.
    keyboard.add(telebot.types.InlineKeyboardButton("Мужской", callback_data="Мужской"))
    keyboard.add(telebot.types.InlineKeyboardButton("Женский", callback_data="Женский"))
    return keyboard
