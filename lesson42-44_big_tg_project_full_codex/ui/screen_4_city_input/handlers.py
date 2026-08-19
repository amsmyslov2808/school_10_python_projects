from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.services import get_city_by_name
from ui.states import TravelStates


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    """Получает текст, введённый пользователем в качестве названия города."""

    city_name = message.text.strip()

    if city_name == "":
        bot.send_message(message.chat.id, "Введите название города.")
        return

    try:
        city = get_city_by_name(city_name)
    except Exception:
        bot.send_message(message.chat.id, "Не удалось найти город. Попробуйте ещё раз позже.")
        return

    if city is None:
        bot.send_message(message.chat.id, "Город не найден. Проверьте название города и попробуйте ещё раз.")
        return

    # Координаты нужны экрану 5 для поиска ближайших городов.
    state.add_data(
        source_city_name=city.name,
        source_city_latitude=city.latitude,
        source_city_longitude=city.longitude,
    )

    from ui.screen_5_nearby_cities.handlers import show_screen_5_nearby_cities

    show_screen_5_nearby_cities(message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_4_city_input)
def callback_screen_4_city_input_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает кнопку возврата из ввода города в главное меню."""

    from ui.screen_1_start.handlers import show_screen_2_main_menu

    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
