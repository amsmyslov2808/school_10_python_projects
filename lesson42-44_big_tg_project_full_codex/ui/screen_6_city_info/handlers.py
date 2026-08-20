import requests
from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from services.screen_6_services import get_selected_city_info
from ui.screen_6_city_info.keyboards import get_screen_6_city_info_keyboard
from ui.screen_6_city_info.texts import get_screen_6_city_info_text
from ui.states import TravelStates


def show_screen_6_city_info(chat_id: int, state: StateContext):
    """Загружает из Википедии описание и изображение выбранного города."""

    with state.data() as data:
        city_name = data["selected_city_name"]

    state.set(TravelStates.screen_6_city_info)
    try:
        description, image_url = get_selected_city_info(city_name)
    except (requests.RequestException, ValueError, KeyError):
        bot.send_message(chat_id, "Не удалось получить информацию о городе.", reply_markup=get_screen_6_city_info_keyboard())
        return

    # Telegram сам скачивает изображение по ссылке. Если оно не отправится,
    # информация о городе всё равно будет показана текстом.
    if image_url is not None:
        try:
            bot.send_photo(chat_id, image_url)
        except Exception:
            pass
    bot.send_message(chat_id, get_screen_6_city_info_text(city_name, description), reply_markup=get_screen_6_city_info_keyboard())


@bot.callback_query_handler(state=TravelStates.screen_6_city_info)
def callback_screen_6_city_info_handler(call: types.CallbackQuery, state: StateContext):
    """Возвращает пользователя из карточки города в меню."""

    from ui.screen_1_start.handlers import show_screen_2_main_menu
    bot.answer_callback_query(call.id)
    show_screen_2_main_menu(call.message.chat.id, state)
