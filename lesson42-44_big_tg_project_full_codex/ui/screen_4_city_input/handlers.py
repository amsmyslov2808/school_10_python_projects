from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from models.city import City
from services.screen_4_services import get_city_by_name
from services.screen_5_services import get_nearby_cities
from ui.screen_1_start.handlers import show_screen_2_main_menu
from ui.screen_4_city_input.keyboards import get_screen_5_nearby_cities_keyboard
from ui.screen_4_city_input.texts import get_screen_5_nearby_cities_text
from ui.states import TravelStates


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    """Получает города из API и показывает экран 5."""

    # Достаём из состояния данные города, который ввёл пользователь.
    with state.data() as data:
        source_city = City(
            name=data["source_city_name"],
            latitude=data["source_city_latitude"],
            longitude=data["source_city_longitude"],
        )

    try:
        # Сервис отправляет запрос в GeoNames и возвращает список объектов City.
        cities = get_nearby_cities(source_city)
    except:
        bot.send_message(
            chat_id,
            "Не удалось загрузить ближайшие города. Попробуйте ещё раз позже.",
        )
        return

    if len(cities) == 0:
        bot.send_message(
            chat_id,
            "Рядом не найдено подходящих городов. Введите другой город.",
        )
        return

    # Сохраняем города, чтобы экран 5 знал, какую кнопку нажал пользователь.
    cities_data = []
    for current_city in cities:
        cities_data.append(current_city.__dict__)

    state.add_data(nearby_cities=cities_data)
    state.set(TravelStates.screen_5_nearby_cities)

    bot.send_message(
        chat_id,
        get_screen_5_nearby_cities_text(cities),
        reply_markup=get_screen_5_nearby_cities_keyboard(len(cities)),
    )


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

    # После получения данных из первого запроса показываем следующий экран.
    show_screen_5_nearby_cities(message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_4_city_input)
def callback_screen_4_city_input_handler(call: types.CallbackQuery, state: StateContext):
    """Обрабатывает кнопку возврата из ввода города в главное меню."""

    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
