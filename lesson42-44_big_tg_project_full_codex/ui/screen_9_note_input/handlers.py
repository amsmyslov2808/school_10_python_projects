from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_9_services import save_trip_note
from ui.screen_9_note_input.texts import get_screen_9_note_input_text
from ui.states import TravelStates


def show_screen_9_note_input(chat_id: int, state: StateContext):
    """Переключает бота в режим ожидания текста заметки."""

    state.set(TravelStates.screen_9_note_input)
    bot.send_message(chat_id, get_screen_9_note_input_text())


@bot.message_handler(state=TravelStates.screen_9_note_input, content_types=["text"])
def message_screen_9_note_input_handler(message: types.Message, state: StateContext):
    """Проверяет и сохраняет заметку пользователя."""

    note = message.text.strip()
    if len(note) > 1000:
        bot.send_message(message.chat.id, "Заметка не должна превышать 1000 символов. Сократите текст и попробуйте ещё раз.")
        return

    with state.data() as data:
        trip_id = data.get("selected_trip_id")
    if not save_trip_note(trip_id, message.from_user.id, note):
        bot.send_message(message.chat.id, "Не удалось сохранить заметку.")
        return

    bot.send_message(message.chat.id, "Заметка успешно сохранена.")
    from ui.screen_8_trip_info.handlers import show_screen_8_trip_info
    show_screen_8_trip_info(message.chat.id, message.from_user.id, state)
