"""Заготовки клавиатур для экранов, открываемых из главного меню."""

import telebot


def get_screen_3_holidays_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт кнопку возврата со страницы праздников в главное меню.

    Клавиатура пока не выводится: обработчик возврата ещё не реализован.
    """

    # Одинаковый callback_data позволит общему обработчику возврата открыть
    # главное меню, когда он будет добавлен в проект.
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_4_city_input_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт кнопку возврата с экрана ввода города.

    Клавиатура пока не выводится: обработчик возврата ещё не реализован.
    """

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard


def get_screen_7_visited_cities_keyboard() -> telebot.types.InlineKeyboardMarkup:
    """Создаёт заготовку клавиатуры для экрана истории поездок.

    Клавиатура пока не выводится, поскольку её кнопки ещё не обрабатываются.
    """

    keyboard = telebot.types.InlineKeyboardMarkup()

    # Заготовка рассчитана на страницу из пяти записей истории.
    for city_number in range(1, 6):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать город {city_number}",
                callback_data=f"screen_7_choose_trip_{city_number}",
            )
        )

    # row размещает кнопки перелистывания рядом, в одной строке.
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            "Назад", callback_data="screen_7_previous_page"
        ),
        telebot.types.InlineKeyboardButton(
            "Вперёд", callback_data="screen_7_next_page"
        ),
    )

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "В главное меню", callback_data="screen_2_main_menu"
        )
    )
    return keyboard
