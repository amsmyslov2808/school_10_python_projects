from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen_3_choose_gender.texts import *


def show_screen_4_input_age(chat_id: int, state: StateContext):
    # Переключаем бота на ввод возраста.
    state.set(BotStates.screen_4_input_age)
    bot.send_message(chat_id, get_text_for_screen_4_input_age())


@bot.callback_query_handler(state=BotStates.screen_3_choose_gender)
def callback_handler_screen_3_choose_gender(
    call: types.CallbackQuery, state: StateContext
):
    # Убираем значок загрузки на нажатой кнопке.
    bot.answer_callback_query(call.id)

    # Сохраняем текст нажатой кнопки: «Мужской» или «Женский».
    state.add_data(gender=call.data)

    # Переходим к вопросу о возрасте.
    show_screen_4_input_age(call.message.chat.id, state)
