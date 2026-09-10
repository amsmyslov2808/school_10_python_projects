"""Обработчики главного меню и функции перехода к его разделам."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.screen_2_main_menu.keyboards import *
from ui.screen_2_main_menu.texts import *

from ui.states import TravelStates

from services.screen_2_services import *


def show_screen_3_holidays(chat_id: int, state: StateContext):
    """Переводит диалог на экран праздников и отправляет его содержимое.

    При сбое внешнего сервиса состояние экрана остаётся прежним.
    """

    try:
        # Сервис сам запрашивает праздники, фильтрует их и сортирует по дате.
        holidays = get_holidays_for_next_7_days()

        # Переходим на новый экран только после успешного ответа внешнего API.
        # При ошибке пользователь останется в главном меню и сможет повторить
        # запрос той же кнопкой.
        state.set(TravelStates.screen_3_holidays)

        # Преобразуем полученный список в текст и показываем экран праздников.
        bot.send_message(
            chat_id,
            get_screen_3_holidays_text(holidays),
            # Клавиатуру пока не выводим: для её кнопки ещё нет обработчика.
            # reply_markup=get_screen_3_holidays_keyboard(),
        )

    except:
        # Сообщаем пользователю, если не удалось получить или показать праздники.
        bot.send_message(
            chat_id,
            "Ошибка в получении праздников с сервера.\nПопробуйте повторить запрос ещё раз через минуту",
            # Клавиатуру пока не выводим: для её кнопки ещё нет обработчика.
            # reply_markup=get_screen_3_holidays_keyboard(),
        )


def show_screen_4_city_input(chat_id: int, state: StateContext):
    """Показывает экран, на котором бот ожидает название города."""

    # В этом состоянии текстовые сообщения принимает обработчик ввода города.
    state.set(TravelStates.screen_4_city_input)
    bot.send_message(
        chat_id,
        get_screen_4_city_input_text(),
        # Клавиатуру пока не выводим: для её кнопки ещё нет обработчика.
        # reply_markup=get_screen_4_city_input_keyboard(),
    )


def show_screen_7_visited_cities(chat_id: int, state: StateContext):
    """Загружает из базы и показывает историю поездок пользователя."""

    try:
        # Telegram ID был сохранён обработчиком кнопки в данных состояния.
        with state.data() as data:
            tg_user_id = data["tg_user_id"]

        # Telegram ID ограничивает выборку поездками текущего пользователя.
        visited_cities = get_all_user_visited_cities(tg_user_id)

        # Состояние меняем только после успешного обращения к базе данных.
        state.set(TravelStates.screen_7_visited_cities)

        bot.send_message(
            chat_id,
            get_screen_7_visited_cities_text(visited_cities),
        )
    except:
        # Ошибка чтения данных состояния, обращения к БД или отправки сообщения
        # не должна завершать работу бота.
        bot.send_message(
            chat_id,
            "Ошибка работы с базой данных. Не удалось загрузить историю поездок. Попробуйте ещё раз позже.",
        )


@bot.callback_query_handler(state=TravelStates.screen_2_main_menu)
def callback_screen_2_main_menu_handler(call: types.CallbackQuery, state: StateContext):
    """Направляет нажатие кнопки главного меню на нужный экран.

    Декоратор ограничивает обработчик состоянием ``screen_2_main_menu``, поэтому
    callback-запросы других экранов сюда не попадут.
    """

    # Подтверждаем получение callback-запроса серверу Telegram, чтобы индикатор
    # загрузки на нажатой кнопке исчез у пользователя.
    bot.answer_callback_query(call.id)

    # Значение call.data совпадает с callback_data соответствующей кнопки.
    if call.data == "screen_2_show_holidays":
        show_screen_3_holidays(call.message.chat.id, state)

    elif call.data == "screen_2_input_city":
        show_screen_4_city_input(call.message.chat.id, state)

    elif call.data == "screen_7_visited_cities":
        # Сохраняем Telegram ID в FSM, чтобы следующий экран получил его через
        # контекст состояния, а не через дополнительный параметр функции.
        state.add_data(tg_user_id=call.from_user.id)
        show_screen_7_visited_cities(call.message.chat.id, state)
