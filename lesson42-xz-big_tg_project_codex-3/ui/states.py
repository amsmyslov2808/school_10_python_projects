from telebot.states import State, StatesGroup


class TravelStates(StatesGroup):
    screen_2_main_menu = State()
    screen_3_holidays = State()
    screen_4_city_input = State()
    screen_5_nearby_cities = State()
    screen_6_city_info = State()
    screen_7_trips = State()
    screen_8_trip_info = State()
    screen_9_note_input = State()
