import telebot


def get_screen2_inline_keyboard() -> telebot.types.InlineKeyboardMarkup:
    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_screen2_hollidays7 = telebot.types.InlineKeyboardButton(
        "Праздники на 7 дней", callback_data="button_screen2_hollidays7"
    )
    button_screen2_visit_city = telebot.types.InlineKeyboardButton(
        "Города куда съездить", callback_data="button_screen2_visit_city"
    )
    button_screen2_travel_history = telebot.types.InlineKeyboardButton(
        "История поездок", callback_data="button_screen2_travel_history"
    )

    inline_reply_keyboard.add(button_screen2_hollidays7)
    inline_reply_keyboard.add(button_screen2_visit_city)
    inline_reply_keyboard.add(button_screen2_travel_history)

    return inline_reply_keyboard
