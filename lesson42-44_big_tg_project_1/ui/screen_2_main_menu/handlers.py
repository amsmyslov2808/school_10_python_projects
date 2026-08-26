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

    При сбое внешнего сервиса остаётся то же состояние экрана: пользователь
    увидит клавиатуру и сможет вернуться в главное меню.
    """

    # Новое состояние определит, какие обработчики активны после перехода.
    state.set(TravelStates.screen_3_holidays)

    try:
        # Сервис сам запрашивает праздники, фильтрует их и сортирует по дате.
        holidays = get_holidays_for_next_7_days()

        # Преобразуем полученный список в текст и показываем экран праздников.
        bot.send_message(
            chat_id,
            get_screen_3_holidays_text(holidays),
            reply_markup=get_screen_3_holidays_keyboard(),
        )

    except:
        # Если внешний API недоступен или ответ не удалось обработать,
        # оставляем пользователю возможность повторить запрос с этого экрана.
        bot.send_message(
            chat_id,
            "Ошибка в получении праздников с сервера.\nПопробуйте повторить запрос ещё раз через минуту",
            reply_markup=get_screen_3_holidays_keyboard(),
        )


def show_screen_4_city_input(chat_id: int, state: StateContext):
    """Показывает экран, на котором бот ожидает название города."""

    # В этом состоянии текстовые сообщения принимает обработчик ввода города.
    state.set(TravelStates.screen_4_city_input)
    bot.send_message(
        chat_id,
        get_screen_4_city_input_text(),
        reply_markup=get_screen_4_city_input_keyboard(),
    )


def show_screen_7_trips(chat_id: int, state: StateContext):
    """Переключает диалог на экран истории поездок."""

    # Экран пока использует демонстрационные данные из texts.py.
    state.set(TravelStates.screen_7_trips)
    bot.send_message(
        chat_id,
        get_screen_7_trips_text(),
        reply_markup=get_screen_7_trips_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_2_main_menu)
def callback_screen_2_main_menu_handler(call: types.CallbackQuery, state: StateContext):
    """Направляет нажатие кнопки главного меню на нужный экран.

    Декоратор ограничивает обработчик состоянием ``screen_2_main_menu``, поэтому
    callback-запросы других экранов сюда не попадут.
    """

    # Подтверждаем Telegram получение callback-запроса, чтобы индикатор загрузки
    # на нажатой кнопке исчез у пользователя.
    bot.answer_callback_query(call.id)

    # Значение call.data совпадает с callback_data соответствующей кнопки.
    if call.data == "screen_2_show_holidays":
        show_screen_3_holidays(call.message.chat.id, state)

    elif call.data == "screen_2_input_city":
        show_screen_4_city_input(call.message.chat.id, state)

    elif call.data == "screen_2_show_trips":
        show_screen_7_trips(call.message.chat.id, state)
