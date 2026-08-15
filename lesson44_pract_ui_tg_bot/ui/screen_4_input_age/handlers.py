from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen_4_input_age.texts import *

from ui.screen_4_input_age.keyboards import *


def show_screen_5_check_all_inputs(chat_id: int, state: StateContext):
    # Переключаем бота на экран проверки данных.
    state.set(BotStates.screen_5_check_all_inputs)

    # Показываем введённые данные и кнопки подтверждения.
    bot.send_message(
        chat_id,
        get_text_for_screen_5_check_all_inputs(state),
        reply_markup=get_inline_keyboard_for_screen_5_check_all_inputs(),
    )


@bot.message_handler(state=BotStates.screen_4_input_age, content_types=["text"])
def message_handler_screen_4_input_age(message: types.Message, state: StateContext):
    # Получаем текст возраста без лишних пробелов.
    age_as_text = message.text.strip()
    age = 0

    try:
        # Превращаем текст, например «15», в число 15.
        age = int(age_as_text)
    except:
        # Если превратить в число не получилось, сообщаем об ошибке.
        bot.send_message(
            message.chat.id, get_error_age_not_int_text_for_screen_4_input_age()
        )
        return

    # Проверяем, подходит ли возраст для регистрации.
    if age < 14 or age > 99:
        bot.send_message(
            message.chat.id, get_error_age_out_of_range_text_for_screen_4_input_age()
        )
        return

    # Сохраняем правильный возраст.
    state.add_data(age=age)

    # Переходим к проверке всех данных.
    show_screen_5_check_all_inputs(message.chat.id, state)
