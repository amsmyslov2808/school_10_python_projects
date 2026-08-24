from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.handlers import show_screen_2_main_menu
from ui.states import TravelStates


@bot.callback_query_handler(state=TravelStates.screen_6_city_info)
def callback_screen_6_city_info_handler(call: types.CallbackQuery, state: StateContext):
    """Возвращает пользователя из карточки города в меню."""

    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
