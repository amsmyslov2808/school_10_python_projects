from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.handlers import show_screen_2_main_menu
from ui.screen_2_main_menu.handlers import show_screen_7_trips
from ui.screen_8_trip_info.texts import get_screen_9_note_input_text
from ui.states import TravelStates


def show_screen_9_note_input(chat_id: int, state: StateContext):
    """Показывает экран ввода заметки."""

    state.set(TravelStates.screen_9_note_input)
    bot.send_message(chat_id, get_screen_9_note_input_text())


@bot.callback_query_handler(state=TravelStates.screen_8_trip_info)
def callback_screen_8_trip_info_handler(call: types.CallbackQuery, state: StateContext):
    """Открывает ввод заметки, историю или главное меню."""

    bot.answer_callback_query(call.id)
    if call.data == "screen_8_write_note":
        show_screen_9_note_input(call.message.chat.id, state)
    elif call.data == "screen_8_back":
        with state.data() as data:
            page = data.get("current_trips_page", 0)
        show_screen_7_trips(call.message.chat.id, call.from_user.id, page, state)
    elif call.data == "screen_8_main_menu":
        show_screen_2_main_menu(call.message.chat.id, state)
