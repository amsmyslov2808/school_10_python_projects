from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_8_trip_info.keyboards import *
from ui.screen_8_trip_info.texts import *
from ui.screen_9_note.keyboards import *
from ui.screen_9_note.texts import *
from ui.states import TravelStates


def show_screen_8_trip_info(chat_id: int, state: StateContext):
    with state.data() as data:
        selected_trip = data["selected_trip"]

    state.set(TravelStates.screen_8_trip_info)
    bot.send_message(
        chat_id,
        get_screen_8_trip_info_text(selected_trip),
        reply_markup=get_screen_8_trip_info_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_9_note_input)
def callback_screen_9_note_input_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)
    show_screen_8_trip_info(call.message.chat.id, state)


@bot.message_handler(state=TravelStates.screen_9_note_input, content_types=["text"])
def message_screen_9_note_input_handler(
    message: types.Message, state: StateContext
):
    note = message.text.strip()

    if len(note) > 1000:
        bot.send_message(
            message.chat.id,
            "Заметка не должна превышать 1000 символов. "
            "Сократите текст и попробуйте ещё раз.",
        )
        return

    if note == "":
        bot.send_message(message.chat.id, "Введите текст заметки.")
        return

    with state.data() as data:
        selected_trip = data["selected_trip"]
        mock_trips = data["mock_trips"]

    selected_trip["note"] = note
    state.add_data(selected_trip=selected_trip, mock_trips=mock_trips)

    bot.send_message(message.chat.id, "Заметка успешно сохранена.")

    show_screen_8_trip_info(message.chat.id, state)
