from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instance import bot

# При импорте этого файла обработчики добавляются в bot.
import ui.screen_1_start.handlers
import ui.screen_2_main_menu.handlers
import ui.screen_4_city_input.handlers

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("TravelHunter запущен")
bot.infinity_polling()
