from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_4_city_input.keyboards import *
from ui.screen_4_city_input.texts import *
from ui.states import TravelStates

from services.screen_4_services import *


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    """Переключает состояние и показывает экран ближайших городов."""

    state.set(TravelStates.screen_5_nearby_cities)

    with state.data() as data:
        start_city = data["start_city"]

    try:
        # Сервис сам запрашивает праздники, фильтрует их и сортирует по дате.
        nearby_cities = get_nearby_cities(start_city)

        state.add_data(nearby_cities=nearby_cities)

        # Преобразуем полученный список в текст и показываем экран праздников.
        bot.send_message(
            chat_id,
            get_screen_5_nearby_cities_text(start_city, nearby_cities),
            reply_markup=get_screen_5_nearby_cities_keyboard(len(nearby_cities)),
        )

    except:
        # Если внешний API недоступен или ответ не удалось обработать,
        # оставляем пользователю возможность повторить запрос с этого экрана.
        bot.send_message(
            chat_id,
            "Ошибка работы с сервером городов.\nПопробуйте повторить запрос ещё раз через минуту",
        )


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    """Получает текст, введённый пользователем в качестве названия города."""

    # message.text содержит текст Telegram-сообщения. Переменная подготовлена
    # для будущего поиска города через API или слой services.
    start_city_name = message.text.strip()

    if start_city_name == "":
        bot.send_message(
            message.chat.id,
            "Ошибка. Название Города не может быть пустым. Введите корректное название города.",
        )
        return

    try:
        # Сервис сам запрашивает праздники, фильтрует их и сортирует по дате.
        start_city = get_city_by_name(start_city_name)

        if start_city == None:
            bot.send_message(
                message.chat.id,
                "Ошибка. Такого города в России не существует. Введите корректное название города.",
            )
            return

        state.add_data(start_city=start_city)

        show_screen_5_nearby_cities(message.chat.id, state)

    except:
        # Если внешний API недоступен или ответ не удалось обработать,
        # оставляем пользователю возможность повторить запрос с этого экрана.
        bot.send_message(
            message.chat.id,
            "Ошибка работы с сервером городов.\nПопробуйте повторить запрос ещё раз через минуту",
        )
