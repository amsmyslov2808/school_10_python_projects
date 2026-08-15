# @test_ui_tg_123_bot
# 8611074222:AAFsz-nRaPvkMWfbdZY1IvO_q9lx6IH6qHc

import telebot
from telebot.storage import StateMemoryStorage

# Токен — пароль бота, который выдаёт BotFather.
BOT_TOKEN = "8611074222:AAFsz-nRaPvkMWfbdZY1IvO_q9lx6IH6qHc"

# Создаём объект бота.
bot = telebot.TeleBot(
    BOT_TOKEN,
    # Здесь временно хранятся состояния и данные пользователей.
    state_storage=StateMemoryStorage(),
    # Разрешаем использовать middleware для передачи state в обработчики.
    use_class_middlewares=True,
)
