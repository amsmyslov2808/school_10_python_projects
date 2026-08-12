from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_4_city_input.texts import *
from ui.states import TravelStates


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_5_nearby_cities)
    bot.send_message(chat_id, get_screen_5_nearby_cities_text())


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    city_name = message.text

    show_screen_5_nearby_cities(message.chat.id, state)
