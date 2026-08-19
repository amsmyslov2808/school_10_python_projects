from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.states import TravelStates


@bot.callback_query_handler(state=TravelStates.screen_3_holidays)
def callback_screen_3_holidays_handler(
    call: types.CallbackQuery, state: StateContext
):
    """Возвращает пользователя из экрана праздников в главное меню."""

    # Импорт внутри функции не создаёт циклический импорт при старте программы.
    from ui.screen_1_start.handlers import show_screen_2_main_menu

    # Убираем индикатор загрузки, который Telegram показывает на кнопке.
    bot.answer_callback_query(call.id)
    # Вызываем общую функцию показа главного меню.
    show_screen_2_main_menu(call.message.chat.id, state)
