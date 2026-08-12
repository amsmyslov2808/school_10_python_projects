import telebot
from telebot.storage import StateMemoryStorage


BOT_TOKEN = "7622684586:AAHP662OK75dgaZ4wGL24I93ywPJffqNdO4"

bot = telebot.TeleBot(
    BOT_TOKEN,
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)
