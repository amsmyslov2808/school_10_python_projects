"""Inline-клавиатура главного меню TravelHunter."""

import telebot


def get_screen_2_main_menu_keyboard():
    """Создаёт клавиатуру с тремя основными разделами приложения."""

    # Inline-клавиатура отображается непосредственно под сообщением бота.
    keyboard = telebot.types.InlineKeyboardMarkup()
    # Каждая кнопка добавляется отдельно, поэтому Telegram размещает их
    # вертикально, по одной кнопке в строке.
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            # callback_data не показывается пользователю: это служебное значение,
            # по которому обработчик понимает, какая кнопка была нажата.
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
    # Возвращаем готовую разметку для передачи в bot.send_message.
    return keyboard
