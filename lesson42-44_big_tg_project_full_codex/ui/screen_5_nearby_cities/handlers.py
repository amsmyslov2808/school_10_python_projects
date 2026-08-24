from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_5_services import save_trip
from services.screen_6_services import get_selected_city_info
from ui.screen_2_main_menu.handlers import show_screen_4_city_input
from ui.screen_5_nearby_cities.keyboards import get_screen_6_city_info_keyboard
from ui.screen_5_nearby_cities.texts import get_screen_6_city_info_text
from ui.states import TravelStates


def show_screen_6_city_info(chat_id: int, state: StateContext):
    """Получает информацию о выбранном городе и показывает экран 6."""

    with state.data() as data:
        city_name = data["selected_city_name"]

    state.set(TravelStates.screen_6_city_info)

    try:
        description, image_url = get_selected_city_info(city_name)
    except:
        bot.send_message(
            chat_id,
            "Не удалось получить информацию о городе.",
            reply_markup=get_screen_6_city_info_keyboard(),
        )
        return

    # Если Wikipedia вернула изображение, отправляем его отдельным сообщением.
    if image_url is not None:
        try:
            bot.send_photo(chat_id, image_url)
        except:
            pass

    bot.send_message(
        chat_id,
        get_screen_6_city_info_text(city_name, description),
        reply_markup=get_screen_6_city_info_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_5_nearby_cities)
def callback_screen_5_nearby_cities_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает выбор города или возврат к его вводу."""

    bot.answer_callback_query(call.id)
    if call.data == "screen_5_back":
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
    show_screen_6_city_info(call.message.chat.id, state)
