"""Обработчик выбора города из списка ближайших вариантов."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.states import TravelStates

from services.screen_5_services import *


@bot.callback_query_handler(state=TravelStates.screen_5_nearby_cities)
def callback_screen_5_nearby_cities_handler(
    call: types.CallbackQuery, state: StateContext
):
    """Сохраняет выбранный город в истории поездок пользователя."""

    # Сразу подтверждаем callback, чтобы Telegram убрал индикатор загрузки.
    bot.answer_callback_query(call.id)

    # callback_data содержит индекс города в сохранённом списке, начиная с нуля.
    city_index = int(call.data)

    # Список был записан в состояние при показе экрана ближайших городов.
    with state.data() as data:
        nearby_cities = data.get("nearby_cities")

    city_name = nearby_cities[city_index].name

    try:
        # Telegram ID связывает новую запись с историей текущего пользователя.
        save_visited_city(call.from_user.id, city_name)
        bot.send_message(
            call.message.chat.id,
            f"Город {city_name} сохранён в истории поездок.",
        )
    except:
        # Ошибки БД показываем пользователю, не останавливая polling бота.
        bot.send_message(
            call.message.chat.id,
            "Ошибка при работе с Базой Данных. Не удалось сохранить поездку. Попробуйте ещё раз позже.",
        )
