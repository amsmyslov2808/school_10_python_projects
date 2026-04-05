import telebot
import telebot.types

import phrases

# 8652329663:AAG4yEdkPrR8jnU9sk0d3mvXemQRdS_c0Kg

# @test_school_10_schedule_bot

bot = telebot.TeleBot("8652329663:AAG4yEdkPrR8jnU9sk0d3mvXemQRdS_c0Kg")


@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, phrases.COMMAND_START_OUTPUT_TEXT)


@bot.message_handler(commands=["schedule"])
def command_schedule_handler(message: telebot.types.Message):
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_monday = telebot.types.KeyboardButton("Понедельник")
    button_tuesday = telebot.types.KeyboardButton("Вторник")
    button_wednesday = telebot.types.KeyboardButton("Среда")
    button_thursday = telebot.types.KeyboardButton("Четверг")
    button_friday = telebot.types.KeyboardButton("Пятница")
    button_saturday = telebot.types.KeyboardButton("Суббота")

    reply_keyboard.add(button_monday)
    reply_keyboard.add(button_tuesday)
    reply_keyboard.add(button_wednesday)
    reply_keyboard.add(button_thursday)
    reply_keyboard.add(button_friday)
    reply_keyboard.add(button_saturday)

    bot.send_message(
        message.chat.id, "Выберите день недели:", reply_markup=reply_keyboard
    )


schedule_dictionary = {
    "понедельник": phrases.MESSAGE_TEXT_SCHEDULE_MONDAY,
    "вторник": phrases.MESSAGE_TEXT_SCHEDULE_TUESDAY,
    "среда": phrases.MESSAGE_TEXT_SCHEDULE_WEDNESDAY,
    "четверг": phrases.MESSAGE_TEXT_SCHEDULE_THURSDAY,
    "пятница": phrases.MESSAGE_TEXT_SCHEDULE_FRIDAY,
    "суббота": phrases.MESSAGE_TEXT_SCHEDULE_SATURDAY,
}


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    input_text = message.text.lower()

    output_text = schedule_dictionary.get(
        input_text, "Ошибка. Расписания на этот день не существует."
    )

    bot.send_message(
        message.chat.id, output_text, reply_markup=telebot.types.ReplyKeyboardRemove()
    )


bot.infinity_polling()
