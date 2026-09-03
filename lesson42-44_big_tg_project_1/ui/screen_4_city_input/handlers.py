"""Обработчики ввода исходного города и показа ближайших вариантов."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.screen_4_city_input.keyboards import *
from ui.screen_4_city_input.texts import *
from ui.states import TravelStates

from services.screen_4_services import *


def show_screen_5_nearby_cities(chat_id: int, state: StateContext):
    """Загружает и показывает города рядом с ранее выбранным городом.

    Исходный город берётся из временных данных состояния, куда его записал
    ``message_screen_4_city_input_handler``. Найденный список также сохраняется,
    чтобы обработчик нажатия мог определить выбранный город по индексу кнопки.
    """

    # Контекстный менеджер даёт доступ к данным текущего пользователя/чата.
    with state.data() as data:
        start_city = data["start_city"]

    try:
        # Сервис передаёт координаты исходного города в GeoNames и возвращает
        # не более пяти подходящих вариантов, отсортированных по расстоянию.
        nearby_cities = get_nearby_cities(start_city)

        # Меняем состояние только после успешного ответа GeoNames. При ошибке
        # пользователь останется на экране ввода и сможет повторить запрос.
        state.set(TravelStates.screen_5_nearby_cities)

        # Сохраняем именно объекты City, чтобы при выборе кнопки не выполнять
        # повторный запрос и не восстанавливать данные из текста сообщения.
        state.add_data(nearby_cities=nearby_cities)

        # Количество найденных городов определяет число кнопок клавиатуры.
        bot.send_message(
            chat_id,
            get_screen_5_nearby_cities_text(start_city, nearby_cities),
            reply_markup=get_screen_5_nearby_cities_keyboard(len(nearby_cities)),
        )

    except:
        # Сообщаем пользователю, если не удалось получить или показать список.
        bot.send_message(
            chat_id,
            "Ошибка работы с сервером городов.\nПопробуйте повторить запрос ещё раз через минуту",
        )


@bot.message_handler(state=TravelStates.screen_4_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):
    """Проверяет введённое название и запускает поиск ближайших городов.

    Обработчик активен только на четвёртом экране и только для текстовых
    сообщений. Некорректный ввод не меняет состояние, поэтому пользователь
    может сразу отправить другое название.
    """

    # Убираем пробелы по краям, чтобы строка из одних пробелов считалась пустой,
    # а случайный пробел после названия не ухудшал поиск.
    start_city_name = message.text.strip()

    # Пустой запрос не отправляем во внешний API.
    if start_city_name == "":
        bot.send_message(
            message.chat.id,
            "Ошибка. Название Города не может быть пустым. Введите корректное название города.",
        )
        return

    try:
        # Получаем нормализованное название и координаты найденного города.
        start_city = get_city_by_name(start_city_name)

        # None является штатным результатом, когда GeoNames ничего не нашёл.
        if start_city == None:
            bot.send_message(
                message.chat.id,
                "Ошибка. Такого города в России не существует. Введите корректное название города.",
            )
            return

        # Временные данные FSM принадлежат конкретному диалогу и будут доступны
        # функции следующего экрана.
        state.add_data(start_city=start_city)

        show_screen_5_nearby_cities(message.chat.id, state)

    except:
        # Если город не удалось получить или показать, оставляем пользователю
        # возможность повторить запрос с этого экрана.
        bot.send_message(
            message.chat.id,
            "Ошибка работы с сервером городов.\nПопробуйте повторить запрос ещё раз через минуту",
        )
