"""Точка входа в приложение TravelHunter."""

from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instance import bot

# Эти импорты нужны не для прямого вызова функций. При загрузке модулей
# декораторы @bot.message_handler и @bot.callback_query_handler регистрируют
# функции-обработчики в общем объекте bot.
import ui.screen_1_start.handlers
import ui.screen_2_main_menu.handlers
import ui.screen_3_holidays.handlers
import ui.screen_4_city_input.handlers
import ui.screen_5_nearby_cities.handlers
import ui.screen_6_city_info.handlers
import ui.screen_7_trips.handlers
import ui.screen_8_trip_info.handlers
import ui.screen_9_note_input.handlers

# StateFilter позволяет ограничивать обработчики текущим состоянием диалога.
bot.add_custom_filter(custom_filters.StateFilter(bot))
# Middleware создаёт и передаёт аргумент StateContext в функции-обработчики.
bot.setup_middleware(StateMiddleware(bot))

# При запуске создаём таблицу trips, если она ещё не создана.
from repositories.database import create_tables

create_tables()

print("TravelHunter запущен")
# Бот постоянно запрашивает у Telegram новые события. При временных ошибках
# infinity_polling продолжает работу и повторяет подключение.
bot.infinity_polling()
