import telebot


def get_screen_3_holidays_keyboard():
    """Создаёт кнопку возврата из экрана праздников в главное меню."""

    # Inline-клавиатура отображается прямо под сообщением бота.
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            # callback_data — служебный идентификатор нажатия, не видимый пользователю.
            "В главное меню", callback_data="screen_3_main_menu"
        )
    )
    return keyboard
