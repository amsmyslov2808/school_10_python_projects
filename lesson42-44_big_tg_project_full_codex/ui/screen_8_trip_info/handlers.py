from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_8_services import get_user_trip
from ui.screen_8_trip_info.keyboards import get_screen_8_trip_info_keyboard
from ui.screen_8_trip_info.texts import get_screen_8_trip_info_text
from ui.states import TravelStates


def show_screen_8_trip_info(chat_id: int, tg_user_id: int, state: StateContext):
    """Показывает подробности выбранной поездки."""

    with state.data() as data:
        trip_id = data.get("selected_trip_id")
    trip = get_user_trip(trip_id, tg_user_id)
    if trip is None:
        bot.send_message(chat_id, "Поездка не найдена.")
        return
    state.set(TravelStates.screen_8_trip_info)
    bot.send_message(chat_id, get_screen_8_trip_info_text(trip), reply_markup=get_screen_8_trip_info_keyboard())


@bot.callback_query_handler(state=TravelStates.screen_8_trip_info)
def callback_screen_8_trip_info_handler(call: types.CallbackQuery, state: StateContext):
    """Открывает ввод заметки, историю или главное меню."""

    bot.answer_callback_query(call.id)
    if call.data == "screen_8_write_note":
        from ui.screen_9_note_input.handlers import show_screen_9_note_input
        show_screen_9_note_input(call.message.chat.id, state)
    elif call.data == "screen_8_back":
        from ui.screen_7_trips.handlers import show_screen_7_trips
        with state.data() as data:
            page = data.get("current_trips_page", 0)
        show_screen_7_trips(call.message.chat.id, call.from_user.id, page, state)
    elif call.data == "screen_8_main_menu":
        from ui.screen_1_start.handlers import show_screen_2_main_menu
        show_screen_2_main_menu(call.message.chat.id, state)
