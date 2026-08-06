from lesson42_big_tg_project_1.ui.screen_1.keyboards import *
from lesson42_big_tg_project_1.ui.screen_1.texts import *
from main import bot


@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    output_text = get_screen2_static_text()

    inline_reply_keyboard = get_screen2_inline_keyboard()

    bot.send_message(message.chat.id, output_text, reply_markup=inline_reply_keyboard)
