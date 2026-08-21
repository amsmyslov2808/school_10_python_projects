import requests

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.screen_2_main_menu.keyboards import *
from ui.screen_2_main_menu.texts import *
from services.screen_2_services import get_holidays_for_next_7_days

from ui.states import TravelStates


def show_screen_3_holidays(chat_id: int, state: StateContext):
    """Переводит диалог на экран праздников и отправляет его содержимое."""

    # После смены состояния нажатие кнопки «В главное меню» обработает экран 3.
    state.set(TravelStates.screen_3_holidays)

    try:
        # Сервис отбирает до семи праздников ближайшей недели, чередуя страны.
        holidays = get_holidays_for_next_7_days()
        # Превращаем объекты Holiday в один текст Telegram-сообщения.
        output_text = get_screen_3_holidays_text(holidays)
    except (requests.RequestException, ValueError, TypeError, KeyError):
        # Не даём боту завершиться с ошибкой, если API недоступно или вернуло
        # данные в неожиданном формате.
        output_text = (
            "Не удалось загрузить праздники. "
            "Проверьте подключение к интернету и попробуйте ещё раз."
        )

    bot.send_message(
        chat_id,
        output_text,
        # Кнопка позволяет покинуть экран праздников и вернуться в меню.
        reply_markup=get_screen_3_holidays_keyboard(),
    )


def show_screen_4_city_input(chat_id: int, state: StateContext):
    """Показывает экран, на котором бот ожидает название города."""

    state.set(TravelStates.screen_4_city_input)
    bot.send_message(
        chat_id,
        get_screen_4_city_input_text(),
        reply_markup=get_screen_4_city_input_keyboard(),
    )


def show_screen_7_trips(chat_id: int, state: StateContext):
    """Переключает диалог на экран истории поездок."""

    state.set(TravelStates.screen_7_trips)
    bot.send_message(
        chat_id,
        get_screen_7_trips_text(),
        reply_markup=get_screen_7_trips_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_2_main_menu)
def callback_screen_2_main_menu_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает нажатия inline-кнопок на экране главного меню."""

    # Подтверждаем Telegram получение callback-запроса, чтобы индикатор загрузки
    # на нажатой кнопке исчез у пользователя.
    bot.answer_callback_query(call.id)

    # Значение call.data совпадает с callback_data соответствующей кнопки.
    if call.data == "screen_2_show_holidays":
        show_screen_3_holidays(call.message.chat.id, state)

    elif call.data == "screen_2_input_city":
        show_screen_4_city_input(call.message.chat.id, state)

    elif call.data == "screen_2_show_trips":
        show_screen_7_trips(call.message.chat.id, state)
"""Переходы из главного меню в выбранные пользователем разделы."""
