import telebot


def get_inline_keyboard_for_screen_5_check_all_inputs():
    # Создаём клавиатуру для подтверждения данных.
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            # Эти данные получит обработчик после нажатия кнопки.
            "Всё верно. Сохранить", callback_data="all_correct"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Ошибки. Отменить сохранение", callback_data="mistakes"
        )
    )
    return keyboard
