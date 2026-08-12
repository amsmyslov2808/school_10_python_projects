from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_2_main_menu.keyboards import get_screen_4_city_input_keyboard
from ui.screen_2_main_menu.texts import get_screen_4_city_input_text
from ui.screen_6_city_info.keyboards import *
from ui.screen_6_city_info.texts import *
from ui.states import TravelStates


def show_screen_4_city_input(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_4_city_input)
    bot.send_message(
        chat_id,
        get_screen_4_city_input_text(),
        reply_markup=get_screen_4_city_input_keyboard(),
    )


def show_screen_6_city_info(chat_id: int, state: StateContext):
    with state.data() as data:
        selected_city = data["selected_city"]

    mock_trip = {
        "date": datetime.now().strftime("%d.%m.%Y"),
        "city": selected_city["name"],
        "note": None,
    }
    state.add_data(last_mock_trip=mock_trip)
    state.set(TravelStates.screen_6_city_info)
    bot.send_message(
        chat_id,
        get_screen_6_city_info_text(selected_city),
        reply_markup=get_screen_6_city_info_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_5_nearby_cities)
def callback_screen_5_nearby_cities_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "screen_5_back":
        show_screen_4_city_input(call.message.chat.id, state)
        return

    city_number = int(call.data.split("_")[-1])

    with state.data() as data:
        cities = data["nearby_cities"]

    selected_city = cities[city_number - 1]
    state.add_data(selected_city=selected_city)

    show_screen_6_city_info(call.message.chat.id, state)
from datetime import datetime
