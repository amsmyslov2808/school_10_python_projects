import telebot


def get_screen_5_nearby_cities_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()

    for city_number in range(1, 6):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_number}",
                callback_data=f"screen_5_choose_city_{city_number}",
            )
        )

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Назад", callback_data="screen_5_back"
        )
    )
    return keyboard


def get_screen_6_city_info_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard
