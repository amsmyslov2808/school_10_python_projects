from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_8_services import get_user_trip
from ui.screen_1_start.handlers import show_screen_2_main_menu
from ui.screen_2_main_menu.handlers import show_screen_7_trips
from ui.screen_7_trips.keyboards import get_screen_8_trip_info_keyboard
from ui.screen_7_trips.texts import get_screen_8_trip_info_text
from ui.states import TravelStates


def show_screen_8_trip_info(chat_id: int, tg_user_id: int, state: StateContext):
    """Получает выбранную поездку и показывает экран 8."""

    with state.data() as data:
        trip_id = data["selected_trip_id"]

    trip = get_user_trip(trip_id, tg_user_id)
    if trip is None:
        bot.send_message(chat_id, "Поездка не найдена.")
        return

    state.set(TravelStates.screen_8_trip_info)
    bot.send_message(
        chat_id,
        get_screen_8_trip_info_text(trip),
        reply_markup=get_screen_8_trip_info_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_7_trips)
def callback_screen_7_trips_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает выбор поездки, страницы или возврат в меню."""

    bot.answer_callback_query(call.id)
    with state.data() as data:
        page = data.get("current_trips_page", 0)
        trip_ids = data.get("current_trips", [])

    if call.data == "screen_7_previous_page":
        show_screen_7_trips(call.message.chat.id, call.from_user.id, page - 1, state)
    elif call.data == "screen_7_next_page":
        show_screen_7_trips(call.message.chat.id, call.from_user.id, page + 1, state)
    elif call.data == "screen_7_main_menu":
        show_screen_2_main_menu(call.message.chat.id, state)
    elif call.data.startswith("screen_7_choose_trip_"):
        trip_index = int(call.data.rsplit("_", 1)[1]) - 1
        if 0 <= trip_index < len(trip_ids):
            state.add_data(selected_trip_id=trip_ids[trip_index])
            show_screen_8_trip_info(call.message.chat.id, call.from_user.id, state)
