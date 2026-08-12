from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.states import TravelStates


@bot.message_handler(commands=["start"])
def command_screen_1_start_handler(message: types.Message, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        message.chat.id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )
