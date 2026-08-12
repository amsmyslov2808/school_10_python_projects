from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import *
from ui.screen_1_start.texts import *
from ui.states import TravelStates


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


@bot.message_handler(commands=["start"])
def command_screen_2_main_menu_handler(message: types.Message, state: StateContext):
    show_screen_2_main_menu(message.chat.id, state)
