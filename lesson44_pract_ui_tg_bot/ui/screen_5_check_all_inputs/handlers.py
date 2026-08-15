from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen_5_check_all_inputs.texts import *


def show_choose_all_correct(chat_id: int):
    # Отправляем сообщение об успешном сохранении.
    bot.send_message(chat_id, get_text_for_choose_all_correct())


def show_choose_mistakes(chat_id: int):
    # Отправляем сообщение об отмене сохранения.
    bot.send_message(chat_id, get_text_for_choose_mistakes())


@bot.callback_query_handler(state=BotStates.screen_5_check_all_inputs)
def callback_handler_screen_5_check_all_inputs(
    call: types.CallbackQuery, state: StateContext
):
    # Убираем значок загрузки на нажатой кнопке.
    bot.answer_callback_query(call.id)

    if call.data == "all_correct":
        # в реальной программе здесь идёт сохранение в базу данных
        # Удаляем состояние и временные данные пользователя.
        state.delete()
        show_choose_all_correct(call.message.chat.id)

    elif call.data == "mistakes":
        # Пользователь отменил регистрацию: очищаем его данные.
        state.delete()
        show_choose_mistakes(call.message.chat.id)
