from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_4_city_input.keyboards import *
from ui.screen_4_city_input.texts import *
from ui.states import TravelStates


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    """Переключает состояние и показывает экран ближайших городов."""

    state.set(TravelStates.screen_5_nearby_cities)
    bot.send_message(
        chat_id,
        get_screen_5_nearby_cities_text(),
        reply_markup=get_screen_5_nearby_cities_keyboard(),
    )


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    """Получает текст, введённый пользователем в качестве названия города."""

    # message.text содержит текст Telegram-сообщения. Переменная подготовлена
    # для будущего поиска города через API или слой services.
    city_name = message.text.strip()

    if city_name == "":
        bot.send_message(message.chat.id, "Введите название города.")
        return

    state.add_data(city_name=city_name)

    # После получения ввода переходим к следующему экрану сценария.
    show_screen_5_nearby_cities(message.chat.id, state)
