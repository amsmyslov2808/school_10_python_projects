import math

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_1_start.keyboards import get_screen_2_main_menu_keyboard
from ui.screen_1_start.texts import get_screen_2_main_menu_text
from ui.screen_7_trips.keyboards import *
from ui.screen_7_trips.texts import *
from ui.screen_8_trip_info.keyboards import *
from ui.screen_8_trip_info.texts import *
from ui.states import TravelStates


TRIPS_ON_PAGE = 5


def show_screen_2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(TravelStates.screen_2_main_menu)
    bot.send_message(
        chat_id,
        get_screen_2_main_menu_text(),
        reply_markup=get_screen_2_main_menu_keyboard(),
    )


def prepare_screen_7_trips(page: int, state: StateContext):
    with state.data() as data:
        mock_trips = data.get("mock_trips", MOCK_TRIPS)
        last_mock_trip = data.get("last_mock_trip")

    if last_mock_trip != None and last_mock_trip not in mock_trips:
        mock_trips = [last_mock_trip] + mock_trips

    total_pages = math.ceil(len(mock_trips) / TRIPS_ON_PAGE)
    page = max(0, min(page, total_pages - 1))
    first_trip_index = page * TRIPS_ON_PAGE
    trips_on_page = mock_trips[first_trip_index : first_trip_index + TRIPS_ON_PAGE]

    state.add_data(
        mock_trips=mock_trips,
        trips_page=page,
        trips_total_pages=total_pages,
        trips_on_page=trips_on_page,
    )

    output_text = get_screen_7_trips_text(trips_on_page, page, total_pages)
    keyboard = get_screen_7_trips_keyboard(trips_on_page, page, total_pages)
    return output_text, keyboard


def show_screen_7_trips(chat_id: int, page: int, state: StateContext):
    output_text, keyboard = prepare_screen_7_trips(page, state)
    state.set(TravelStates.screen_7_trips)
    bot.send_message(chat_id, output_text, reply_markup=keyboard)


def show_screen_8_trip_info(chat_id: int, state: StateContext):
    with state.data() as data:
        selected_trip = data["selected_trip"]

    state.set(TravelStates.screen_8_trip_info)
    bot.send_message(
        chat_id,
        get_screen_8_trip_info_text(selected_trip),
        reply_markup=get_screen_8_trip_info_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_7_trips)
def callback_screen_7_trips_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    with state.data() as data:
        page = data.get("trips_page", 0)
        trips_on_page = data.get("trips_on_page", [])

    if call.data == "screen_7_main_menu":
        show_screen_2_main_menu(call.message.chat.id, state)
    elif call.data == "screen_7_previous_page":
        show_screen_7_trips(call.message.chat.id, page - 1, state)
    elif call.data == "screen_7_next_page":
        show_screen_7_trips(call.message.chat.id, page + 1, state)
    elif call.data.startswith("screen_7_choose_trip_"):
        trip_number = int(call.data.split("_")[-1])
        selected_trip = trips_on_page[trip_number - 1]
        state.add_data(selected_trip=selected_trip)

        show_screen_8_trip_info(call.message.chat.id, state)
