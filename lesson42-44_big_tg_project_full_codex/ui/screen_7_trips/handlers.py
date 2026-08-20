from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_7_services import get_user_trips
from ui.screen_7_trips.keyboards import get_screen_7_trips_keyboard
from ui.screen_7_trips.texts import get_screen_7_trips_text
from ui.states import TravelStates

TRIPS_PER_PAGE = 5


def show_screen_7_trips(chat_id: int, tg_user_id: int, page: int, state: StateContext):
    """Показывает выбранную страницу истории поездок."""

    try:
        all_trips = get_user_trips(tg_user_id)
    except Exception:
        bot.send_message(chat_id, "Не удалось загрузить историю поездок. Попробуйте ещё раз позже.")
        return

    first_trip = page * TRIPS_PER_PAGE
    trips = all_trips[first_trip:first_trip + TRIPS_PER_PAGE]
    state.add_data(current_trips=[trip.id for trip in trips], current_trips_page=page)
    state.set(TravelStates.screen_7_trips)
    bot.send_message(chat_id, get_screen_7_trips_text(trips, page), reply_markup=get_screen_7_trips_keyboard(len(trips), page, len(all_trips) > first_trip + TRIPS_PER_PAGE))


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
        from ui.screen_1_start.handlers import show_screen_2_main_menu
        show_screen_2_main_menu(call.message.chat.id, state)
    elif call.data.startswith("screen_7_choose_trip_"):
        trip_index = int(call.data.rsplit("_", 1)[1]) - 1
        if 0 <= trip_index < len(trip_ids):
            state.add_data(selected_trip_id=trip_ids[trip_index])
            from ui.screen_8_trip_info.handlers import show_screen_8_trip_info
            show_screen_8_trip_info(call.message.chat.id, call.from_user.id, state)
