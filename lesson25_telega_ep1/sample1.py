import telebot
import telebot.types

from datetime import datetime

# 8778031926:AAHp9_QT6s_CghrZto8l3wuJjnPJvXF5xfY

bot = telebot.TeleBot("8778031926:AAHp9_QT6s_CghrZto8l3wuJjnPJvXF5xfY")


@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработано сообщение старт")


@bot.message_handler(commands=["reply"])
def command_start_handler(message: telebot.types.Message):
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_add_task = telebot.types.KeyboardButton("Добавить задачу")
    button_show_my_tasks = telebot.types.KeyboardButton("Мои задачи")

    reply_keyboard.add(button_add_task)
    reply_keyboard.add(button_show_my_tasks)

    bot.send_message(message.chat.id, "выбери действие:", reply_markup=reply_keyboard)


@bot.message_handler(func=lambda message: message.text == "Добавить задачу")
def message_text_poka_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработал кнопку Добавить задачу")


@bot.message_handler(func=lambda message: message.text == "Мои задачи")
def message_text_poka_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработал кнопку Мои задачи")


@bot.message_handler(commands=["inline"])
def command_start_handler(message: telebot.types.Message):
    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_add_task = telebot.types.InlineKeyboardButton(
        "Добавить задачу", callback_data="button_add_task"
    )
    button_show_my_tasks = telebot.types.InlineKeyboardButton(
        "Мои задачи", callback_data="button_show_my_tasks"
    )

    inline_reply_keyboard.add(button_add_task)
    inline_reply_keyboard.add(button_show_my_tasks)

    bot.send_message(
        message.chat.id, "выбери действие:", reply_markup=inline_reply_keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "button_add_task")
def callback_button_add_task_handler(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "обработал инлайн кнопку Добавить задачу")


@bot.callback_query_handler(func=lambda call: call.data == "button_show_my_tasks")
def callback_button_add_task_handler(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "обработал инлайн кнопку Мои задачи")


@bot.message_handler(func=lambda message: message.text.lower() == "пока")
def message_text_poka_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "я поймал сообщение пока")


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    input_text = message.text.lower()
    output_text = ""

    if input_text == "привет":
        output_text = "ну привет!"
    elif input_text == "время":
        output_text = str(datetime.now())
    elif input_text == "как тебя зовут":
        output_text = "Я бот 111"
    else:
        output_text = "неизвестное сообщение"

    bot.send_message(message.chat.id, output_text)


bot.infinity_polling()
# print("бот запущен")
