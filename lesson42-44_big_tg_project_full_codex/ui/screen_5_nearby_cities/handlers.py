from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from models.city import City
from services.screen_5_services import get_nearby_cities, save_trip
from ui.screen_5_nearby_cities.keyboards import get_screen_5_nearby_cities_keyboard
from ui.screen_5_nearby_cities.texts import get_screen_5_nearby_cities_text
from ui.states import TravelStates


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    """Находит города рядом с введённым пользователем городом."""

    with state.data() as data:
        source_city = City(
            data["source_city_name"],
            data["source_city_latitude"],
            data["source_city_longitude"],
        )

    try:
        cities = get_nearby_cities(source_city)
    except Exception:
        bot.send_message(chat_id, "Не удалось загрузить ближайшие города. Попробуйте ещё раз позже.")
        return

    if len(cities) == 0:
        bot.send_message(chat_id, "Рядом не найдено подходящих городов. Введите другой город.")
        return

    # В state сохраняем простые словари: их легко использовать после нажатия кнопки.
    state.add_data(nearby_cities=[city.__dict__ for city in cities])
    state.set(TravelStates.screen_5_nearby_cities)
    bot.send_message(chat_id, get_screen_5_nearby_cities_text(cities), reply_markup=get_screen_5_nearby_cities_keyboard(len(cities)))


@bot.callback_query_handler(state=TravelStates.screen_5_nearby_cities)
def callback_screen_5_nearby_cities_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает выбор города или возврат к его вводу."""

    bot.answer_callback_query(call.id)
    if call.data == "screen_5_back":
        from ui.screen_2_main_menu.handlers import show_screen_4_city_input
        show_screen_4_city_input(call.message.chat.id, state)
        return

    if not call.data.startswith("screen_5_choose_city_"):
        return

    city_index = int(call.data.rsplit("_", 1)[1]) - 1
    with state.data() as data:
        cities = data.get("nearby_cities", [])
    if city_index < 0 or city_index >= len(cities):
        bot.send_message(call.message.chat.id, "Город не найден. Попробуйте выбрать его ещё раз.")
        return

    city_name = cities[city_index]["name"]
    try:
        save_trip(call.from_user.id, city_name)
    except Exception:
        bot.send_message(call.message.chat.id, "Не удалось сохранить поездку. Попробуйте ещё раз позже.")
        return

    state.add_data(selected_city_name=city_name)
    from ui.screen_6_city_info.handlers import show_screen_6_city_info
    show_screen_6_city_info(call.message.chat.id, state)
