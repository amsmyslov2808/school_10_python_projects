"""Обработчик команды ``/start`` и функция показа главного меню."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.states import TravelStates


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    """Переключает диалог на главное меню и отправляет его содержимое.

    Функция вынесена отдельно, потому что главное меню нужно показывать не
    только после ``/start``, но и после возврата с других экранов.
    """

    # Следующие нажатия кнопок должен принимать обработчик главного меню.
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


@bot.message_handler(commands=["start"])
def command_screen_1_start_handler(message: types.Message, state: StateContext):
    """Сбрасывает прошлый сценарий пользователя и показывает главное меню."""

    # Удаляем старое состояние и связанные с ним временные данные. Благодаря
    # этому /start одинаково работает из любой точки диалога.
    state.delete()
    # Показываем главное меню после очистки предыдущего сценария.
    show_screen_2_main_menu(message.chat.id, state)
