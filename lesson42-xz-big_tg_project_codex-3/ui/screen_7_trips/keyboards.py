import telebot


def get_screen_7_trips_keyboard(trips: list[dict], page: int, total_pages: int):
    keyboard = telebot.types.InlineKeyboardMarkup()

    for trip_number in range(1, len(trips) + 1):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {trip_number}",
                callback_data=f"screen_7_choose_trip_{trip_number}",
            )
        )

    pagination_buttons = []

    if page > 0:
        pagination_buttons.append(
            telebot.types.InlineKeyboardButton(
                "Назад", callback_data="screen_7_previous_page"
            )
        )

    if page < total_pages - 1:
        pagination_buttons.append(
            telebot.types.InlineKeyboardButton(
                "Вперёд", callback_data="screen_7_next_page"
            )
        )

    if pagination_buttons:
        keyboard.row(*pagination_buttons)

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_7_main_menu"
        )
    )
    return keyboard
