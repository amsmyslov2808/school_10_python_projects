from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.states import TravelStates


@bot.message_handler(commands=["start"])
def command_screen_1_start_handler(message: types.Message, state: StateContext):
    """Сбрасывает прошлый сценарий пользователя и показывает главное меню."""

    # Удаляем старое состояние и связанные с ним временные данные. Благодаря
    # этому /start одинаково работает из любой точки диалога.
    state.delete()
    # Следующие callback-запросы должны обрабатываться как события главного меню.
    state.set(TravelStates.screen_2_main_menu)
    # chat.id определяет чат-получатель, а reply_markup прикрепляет inline-кнопки.
    bot.send_message(
        message.chat.id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )
"""Обработчик команды /start и перехода в главное меню."""
