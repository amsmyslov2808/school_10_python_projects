from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.screen_7_trips.handlers import prepare_screen_7_trips
from ui.screen_8_trip_info.keyboards import *
from ui.screen_8_trip_info.texts import *
from ui.screen_9_note.keyboards import *
from ui.screen_9_note.texts import *
from ui.states import TravelStates


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


def show_screen_7_trips(chat_id: int, page: int, state: StateContext):
    output_text, keyboard = prepare_screen_7_trips(page, state)
    state.set(TravelStates.screen_7_trips)
    bot.send_message(chat_id, output_text, reply_markup=keyboard)


def show_screen_9_note_input(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_9_note_input)
    bot.send_message(
        chat_id,
        get_screen_9_note_input_text(),
        reply_markup=get_screen_9_note_input_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_8_trip_info)
def callback_screen_8_trip_info_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "screen_8_write_note":
        show_screen_9_note_input(call.message.chat.id, state)
    elif call.data == "screen_8_back":
        with state.data() as data:
            page = data.get("trips_page", 0)

        show_screen_7_trips(call.message.chat.id, page, state)
    elif call.data == "screen_8_main_menu":
        show_screen_2_main_menu(call.message.chat.id, state)
