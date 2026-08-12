from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_4_city_input.keyboards import *
from ui.screen_4_city_input.texts import *
from ui.states import TravelStates


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_5_nearby_cities)
    bot.send_message(
        chat_id,
        get_screen_5_nearby_cities_text(),
        reply_markup=get_screen_5_nearby_cities_keyboard(),
    )


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    city_name = message.text.strip()

    if city_name == "":
        bot.send_message(message.chat.id, "Введите название города.")
        return

    state.add_data(city_name=city_name)

    show_screen_5_nearby_cities(message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_4_city_input)
def callback_screen_4_city_input_handler(
    call: types.CallbackQuery, state: StateContext
):
    from ui.screen_1_start.handlers import show_screen_2_main_menu

    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_5_nearby_cities)
def callback_screen_5_nearby_cities_handler(
    call: types.CallbackQuery, state: StateContext
):
    from ui.screen_2_main_menu.handlers import show_screen_4_city_input

    bot.answer_callback_query(call.id)

    if call.data == "screen_5_back":
        show_screen_4_city_input(call.message.chat.id, state)
    elif call.data.startswith("screen_5_choose_city_"):
        state.set(TravelStates.screen_6_city_info)
        bot.send_message(
            call.message.chat.id,
            "Прекрасный выбор!\n\n"
            "Бердск — небольшой город на берегу Новосибирского водохранилища. "
            "Здесь можно прогуляться по набережной и хорошо провести выходной.",
            reply_markup=get_screen_6_city_info_keyboard(),
        )


@bot.callback_query_handler(state=TravelStates.screen_6_city_info)
def callback_screen_6_city_info_handler(
    call: types.CallbackQuery, state: StateContext
):
    from ui.screen_1_start.handlers import show_screen_2_main_menu

    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
