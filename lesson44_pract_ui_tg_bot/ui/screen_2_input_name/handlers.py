from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen_2_input_name.texts import *

from ui.screen_2_input_name.keyboards import *


def show_screen_3_choose_gender(chat_id: int, state: StateContext):
    # Переключаем бота на выбор пола.
    state.set(BotStates.screen_3_choose_gender)

    # Отправляем сообщение с кнопками выбора.
    bot.send_message(
        chat_id,
        get_text_for_screen_3_choose_gender(),
        reply_markup=get_inline_keyboard_for_screen_3_choose_gender(),
    )


@bot.message_handler(state=BotStates.screen_2_input_name, content_types=["text"])
def message_handler_screen_2_input_name(message: types.Message, state: StateContext):
    # Убираем лишние пробелы в начале и конце имени.
    name = message.text.strip()

    # Имя должно состоять из 2–25 символов.
    if len(name) < 2 or len(name) > 25:
        bot.send_message(message.chat.id, get_error_name_text_for_screen_2_input_name())
        return

    # Сохраняем имя в данных текущего пользователя.
    state.add_data(name=name)

    # Переходим к следующему вопросу.
    show_screen_3_choose_gender(message.chat.id, state)
