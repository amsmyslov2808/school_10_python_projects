from telebot.states import State, StatesGroup


class BotStates(StatesGroup):
    # Этапы регистрации пользователя в боте.
    screen_2_input_name = State()
    screen_3_choose_gender = State()
    screen_4_input_age = State()
    screen_5_check_all_inputs = State()
