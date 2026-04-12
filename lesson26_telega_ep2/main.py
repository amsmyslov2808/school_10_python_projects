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

import random

used_numbers = set()


def generate_unique_number():
    while True:
        number = random.randint(1000, 9999)

        if number not in used_numbers:
            used_numbers.add(number)
            return number


bot = telebot.TeleBot(
    "7974872453:AAFQHoSf7MQyT_AwZV0kreyhIFi5gY6rob4",
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


registrations_dictionary = {}
# MAX_TELEGRAM_MESSAGE_LENGTH = 4096
MAX_TELEGRAM_MESSAGE_LENGTH = 300
ADMIN_RETURN_TO_MENU_TEXT = "\n\n\nВернитесь в главное меню путём ввода команды /start"


class RegistrationStates(StatesGroup):
    main_menu_buttons_press = State()
    input_team_title = State()
    input_team_count_members = State()
    input_team_chosen_task = State()
    save_team_data = State()
    check_admin_password = State()


def get_registered_teams_lines():
    lines = []

    for unique_key, data in registrations_dictionary.items():
        lines.append(
            f"Команда: {data['title']} Количество человек: {data['count_members']} Выбранная задача: {data['chosen_task']} (ИД команды: {unique_key})"
        )

    return lines


def split_text_lines_to_pages(lines):
    reserved_length_for_footer_and_page_info = len(ADMIN_RETURN_TO_MENU_TEXT) + 40
    max_page_body_length = (
        MAX_TELEGRAM_MESSAGE_LENGTH - reserved_length_for_footer_and_page_info
    )

    pages = []
    current_page_lines = []
    current_page_length = 0

    for line in lines:
        line_length_with_separator = len(line) + (1 if current_page_lines else 0)

        if (
            current_page_lines
            and current_page_length + line_length_with_separator > max_page_body_length
        ):
            pages.append("\n".join(current_page_lines))
            current_page_lines = [line]
            current_page_length = len(line)
            continue

        current_page_lines.append(line)
        current_page_length += line_length_with_separator

    if current_page_lines:
        pages.append("\n".join(current_page_lines))

    return pages


def get_admin_page_text(page_text, page_index, total_pages):
    return (
        f"{page_text}{ADMIN_RETURN_TO_MENU_TEXT}\n\n"
        f"Страница {page_index + 1}/{total_pages}"
    )


def build_admin_pagination_keyboard(page_index, total_pages):
    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()
    buttons = []

    if page_index > 0:
        buttons.append(
            telebot.types.InlineKeyboardButton(
                "⬅️ Назад", callback_data="admin_prev_page"
            )
        )

    if page_index < total_pages - 1:
        buttons.append(
            telebot.types.InlineKeyboardButton(
                "Вперёд ➡️", callback_data="admin_next_page"
            )
        )

    if buttons:
        inline_reply_keyboard.row(*buttons)

    return inline_reply_keyboard


@bot.message_handler(commands=["start", "cancel_registration"])
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

    state.delete()
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
    elif call.data == "button_show_all_teams":
        output_text = "Пожалуйста введи пароль чтобы получить доступ к списку зарегистрированных команд"

        state.set(RegistrationStates.check_admin_password)

        bot.send_message(call.message.chat.id, output_text)


@bot.message_handler(state=RegistrationStates.check_admin_password)
def message_check_admin_password_handler(message: types.Message, state: StateContext):
    password = message.text.strip()

    if password != "12345":
        output_text = "Ошибка. Пароль неверный. Повторите ввод ещё раз или вернитесь в главное меню путём ввода команды /start"
        bot.send_message(message.chat.id, output_text)
        return

    if len(registrations_dictionary) == 0:
        output_text = (
            "Записей пока нет. Вернитесь в главное меню путём ввода команды /start"
        )
        bot.send_message(message.chat.id, output_text)
        return

    lines = get_registered_teams_lines()
    output_text = "\n".join(lines) + ADMIN_RETURN_TO_MENU_TEXT

    if len(output_text) <= MAX_TELEGRAM_MESSAGE_LENGTH:
        bot.send_message(message.chat.id, output_text)
        return

    pages = split_text_lines_to_pages(lines)
    current_page_index = 0

    state.add_data(admin_pages=pages, admin_current_page=current_page_index)

    current_page_text = get_admin_page_text(
        pages[current_page_index], current_page_index, len(pages)
    )
    inline_reply_keyboard = build_admin_pagination_keyboard(
        current_page_index, len(pages)
    )

    bot.send_message(
        message.chat.id, current_page_text, reply_markup=inline_reply_keyboard
    )


@bot.callback_query_handler(
    func=lambda call: call.data in ["admin_prev_page", "admin_next_page"],
    state=RegistrationStates.check_admin_password,
)
def callback_admin_pagination_handler(call: types.CallbackQuery, state: StateContext):
    with state.data() as data:
        pages = data.get("admin_pages")
        current_page = data.get("admin_current_page", 0)

    if not pages:
        bot.answer_callback_query(
            call.id,
            "Список команд не найден. Введите пароль ещё раз.",
            show_alert=False,
        )
        return

    if call.data == "admin_prev_page" and current_page > 0:
        current_page -= 1
    elif call.data == "admin_next_page" and current_page < len(pages) - 1:
        current_page += 1

    state.add_data(admin_current_page=current_page)

    output_text = get_admin_page_text(pages[current_page], current_page, len(pages))
    inline_reply_keyboard = build_admin_pagination_keyboard(current_page, len(pages))

    bot.edit_message_text(
        output_text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=inline_reply_keyboard,
    )
    bot.answer_callback_query(call.id)


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
        unique_key = generate_unique_number()

        with state.data() as data:
            registrations_dictionary[unique_key] = {
                "title": data["title"],
                "count_members": data["count_members"],
                "chosen_task": data["chosen_task"],
            }

        output_text = f"Данные успешно сохранены\nИД вашей команды = {unique_key} Сохраните его\nНажите /start для перехода в главное меню"

    elif call.data == "button_no":

        output_text = "Данные не сохранены\nНажите /start для перехода в главное меню"

    state.delete()

    bot.send_message(call.message.chat.id, output_text)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()
