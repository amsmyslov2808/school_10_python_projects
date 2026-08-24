from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_9_services import save_trip_note
from ui.screen_7_trips.handlers import show_screen_8_trip_info
from ui.states import TravelStates


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
    show_screen_8_trip_info(message.chat.id, message.from_user.id, state)
