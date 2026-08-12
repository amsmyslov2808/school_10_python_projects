from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.screen_6_city_info.keyboards import *
from ui.screen_6_city_info.texts import *
from ui.states import TravelStates


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_6_city_info)
def callback_screen_6_city_info_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
