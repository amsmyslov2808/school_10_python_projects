import requests
from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.services import get_holidays_for_next_30_days
from ui.screen_2_main_menu.keyboards import *
from ui.screen_2_main_menu.texts import *
from ui.states import TravelStates


def show_screen_3_holidays(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_3_holidays)

    try:
        holidays = get_holidays_for_next_30_days()
        output_text = get_screen_3_holidays_text(holidays)
    except (requests.RequestException, ValueError, TypeError, KeyError):
        output_text = (
            "Не удалось загрузить праздники. "
            "Проверьте подключение к интернету и попробуйте ещё раз."
        )

    bot.send_message(
        chat_id,
        output_text,
        reply_markup=get_screen_3_holidays_keyboard(),
    )


def show_screen_4_city_input(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_4_city_input)
    bot.send_message(
        chat_id,
        get_screen_4_city_input_text(),
        reply_markup=get_screen_4_city_input_keyboard(),
    )


def show_screen_7_trips(chat_id: int, state: StateContext):
    from ui.screen_7_trips.handlers import prepare_screen_7_trips

    output_text, keyboard = prepare_screen_7_trips(0, state)
    state.set(TravelStates.screen_7_trips)
    bot.send_message(chat_id, output_text, reply_markup=keyboard)


@bot.callback_query_handler(state=TravelStates.screen_2_main_menu)
def callback_screen_2_main_menu_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "screen_2_show_holidays":
        show_screen_3_holidays(call.message.chat.id, state)

    elif call.data == "screen_2_input_city":
        show_screen_4_city_input(call.message.chat.id, state)

    elif call.data == "screen_2_show_trips":
        show_screen_7_trips(call.message.chat.id, state)
