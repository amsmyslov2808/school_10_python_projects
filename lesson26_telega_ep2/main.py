# 7974872453:AAFQHoSf7MQyT_AwZV0kreyhIFi5gY6rob4

# start
# cancel_registration

# @test_school_10_register_hack_bot

import telebot
from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage


bot = telebot.TeleBot(
    "",
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


registrations_dictionary = {}


class RegistrationStates(StatesGroup):
    main_menu_buttons_press = State()
    input_team_title = State()
    input_team_count_members = State()
    input_team_chosen_task = State()
    save_team_data = State()


@bot.message_handler(commands=["start"])
def command_start_handler(message: types.Message, state: StateContext):

    output_text = "Приветствуем вас на регистрации Хакатона!\nВыберите нужное действие:"

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_add_team = telebot.types.InlineKeyboardButton(
        "Добавить новую команду", callback_data="button_add_team"
    )
    button_show_all_teams = telebot.types.InlineKeyboardButton(
        "Просмотреть все добавленные команды", callback_data="button_show_all_teams"
    )

    inline_reply_keyboard.add(button_add_team)
    inline_reply_keyboard.add(button_show_all_teams)

    state.set(RegistrationStates.main_menu_buttons_press)

    bot.send_message(message.chat.id, output_text, reply_markup=inline_reply_keyboard)


@bot.callback_query_handler(state=RegistrationStates.main_menu_buttons_press)
def callback_buttons_main_menu_team_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "button_add_team":
        output_text = (
            "Пожалуйста введи название вашей команды. (от 1 до 30 символов длинной)"
        )

        state.set(RegistrationStates.input_team_title)

        bot.send_message(call.message.chat.id, output_text)


@bot.message_handler(state=RegistrationStates.input_team_title)
def message_text_team_title_handler(message: types.Message, state: StateContext):
    title = message.text.strip()

    if len(title) > 30:
        output_text = "Ошибка. Длина названия команды должна быть от 1 до 30 символов\nВведите название ещё раз"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(title=title)

    output_text = (
        "Введите количество участников вашей команде( от 1-го до 4-х человек): "
    )

    state.set(RegistrationStates.input_team_count_members)

    bot.send_message(
        message.chat.id,
        output_text,
    )


@bot.message_handler(state=RegistrationStates.input_team_count_members)
def message_text_team_title_handler(message: types.Message, state: StateContext):
    count_members_as_text = message.text.strip()

    if count_members_as_text.isdigit() == False:
        output_text = "Ошибка. Вы ввели НЕ число. Попробуйте ещё раз:"
        bot.send_message(message.chat.id, output_text)
        return

    count_members = int(count_members_as_text)

    if count_members < 1 or count_members > 4:
        output_text = "Ошибка. Количество участников в команде от 1-х до 4-х"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(count_members=count_members)

    output_text = "Выберите решаемую задачу"

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_chat_bot_task = telebot.types.InlineKeyboardButton(
        "Чат-бот", callback_data="Чат-бот"
    )
    button_application_task = telebot.types.InlineKeyboardButton(
        "Веб или мобильное приложение", callback_data="Веб или мобильное приложение"
    )
    button_complex_system_task = telebot.types.InlineKeyboardButton(
        "Комплексная система", callback_data="Комплексная система"
    )

    inline_reply_keyboard.add(button_chat_bot_task)
    inline_reply_keyboard.add(button_application_task)
    inline_reply_keyboard.add(button_complex_system_task)

    state.set(RegistrationStates.input_team_chosen_task)

    bot.send_message(message.chat.id, output_text, reply_markup=inline_reply_keyboard)


@bot.callback_query_handler(state=RegistrationStates.input_team_chosen_task)
def callback_buttons_team_chosen_task_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    state.add_data(chosen_task=call.data)

    with state.data() as data:
        title = data["title"]
        count_members = data["count_members"]
        chosen_task = data["chosen_task"]

    output_text = f"""
Проверьте правильность введённых данных
Название команды: {title}
Количество участников в команде: {count_members}
Выбранная задача: {chosen_task}

Сохранить введённые данные?
"""

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_yes = telebot.types.InlineKeyboardButton("Да", callback_data="button_yes")
    button_no = telebot.types.InlineKeyboardButton("Нет", callback_data="button_no")

    inline_reply_keyboard.add(button_yes)
    inline_reply_keyboard.add(button_no)

    state.set(RegistrationStates.save_team_data)

    bot.send_message(
        call.message.chat.id, output_text, reply_markup=inline_reply_keyboard
    )


@bot.callback_query_handler(state=RegistrationStates.save_team_data)
def callback_buttons_save_team_data_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "button_yes":
        user_id = call.from_user.id

        with state.data() as data:
            registrations_dictionary[user_id] = {
                "title": data["title"],
                "count_members": data["count_members"],
                "chosen_task": data["chosen_task"],
            }

        output_text = (
            "Данные успешно сохранены\nНажите /start для перехода в главное меню"
        )

    elif call.data == "button_no":

        output_text = "Данные не сохранены\nНажите /start для перехода в главное меню"

    state.delete()

    bot.send_message(call.message.chat.id, output_text)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()
