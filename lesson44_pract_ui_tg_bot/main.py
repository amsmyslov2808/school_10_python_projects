from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instance import bot

# Импортируем обработчики всех экранов, чтобы бот их зарегистрировал.
import ui.screen_1_start.handlers
import ui.screen_2_input_name.handlers
import ui.screen_3_choose_gender.handlers
import ui.screen_4_input_age.handlers
import ui.screen_5_check_all_inputs.handlers

# Фильтр позволяет запускать обработчики для нужного состояния.
bot.add_custom_filter(custom_filters.StateFilter(bot))
# Middleware передаёт переменную state в функции-обработчики.
bot.setup_middleware(StateMiddleware(bot))

print("бот запущен")
# Бот постоянно ждёт новые сообщения от Telegram.
bot.infinity_polling()
