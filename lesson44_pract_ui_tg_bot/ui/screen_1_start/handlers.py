from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen_1_start.texts import *


def show_screen_2_input_name(chat_id: int, state: StateContext):
    # Удаляем старые данные, если пользователь начинает регистрацию заново.
    state.delete()
    # Переключаем бота на ввод имени.
    state.set(BotStates.screen_2_input_name)
    # Отправляем вопрос пользователю.
    bot.send_message(chat_id, get_text_for_screen_2_input_name())


@bot.message_handler(commands=["start"])
def command_handler_screen_1_start(message: types.Message, state: StateContext):
    # Команда /start начинает регистрацию.
    show_screen_2_input_name(message.chat.id, state)
