from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.screen_5_nearby_cities.keyboards import *
from ui.screen_5_nearby_cities.texts import *
from ui.states import TravelStates


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    cities = MOCK_NEARBY_CITIES
    state.add_data(nearby_cities=cities)
    state.set(TravelStates.screen_5_nearby_cities)
    bot.send_message(
        chat_id,
        get_screen_5_nearby_cities_text(cities),
        reply_markup=get_screen_5_nearby_cities_keyboard(cities),
    )


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    city_name = message.text.strip()

    if city_name == "":
        bot.send_message(message.chat.id, "Введите название города.")
        return

    state.add_data(city_name=city_name)

    show_screen_5_nearby_cities(message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_4_city_input)
def callback_screen_4_city_input_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
