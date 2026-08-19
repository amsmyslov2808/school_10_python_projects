import telebot


def get_screen_7_trips_keyboard(trips_count: int, page: int, has_next_page: bool):
    """Создаёт кнопки выбора поездок и доступные кнопки пагинации."""

    keyboard = telebot.types.InlineKeyboardMarkup()
    for trip_number in range(1, trips_count + 1):
        keyboard.add(telebot.types.InlineKeyboardButton(f"Выбрать город {trip_number}", callback_data=f"screen_7_choose_trip_{trip_number}"))
    if page > 0:
        keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="screen_7_previous_page"))
    if has_next_page:
        keyboard.add(telebot.types.InlineKeyboardButton("Вперёд", callback_data="screen_7_next_page"))
    keyboard.add(telebot.types.InlineKeyboardButton("В главное меню", callback_data="screen_7_main_menu"))
    return keyboard
