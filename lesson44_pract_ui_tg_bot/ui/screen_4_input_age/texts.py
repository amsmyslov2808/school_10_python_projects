from telebot.states.sync.context import StateContext


def get_error_age_not_int_text_for_screen_4_input_age():
    # Сообщение, если вместо возраста написан не номер.
    return "Ошибка при вводе возраста. Вы ввели не число"


def get_error_age_out_of_range_text_for_screen_4_input_age():
    # Сообщение, если возраст выходит за допустимые границы.
    return "Ошибка при вводе возраста. Вы ввели возраст меньше 14 или больше 99 лет"


def get_text_for_screen_5_check_all_inputs(state: StateContext):
    # Берём все сохранённые данные пользователя из state.
    with state.data() as data:
        name = data.get("name")
        gender = data.get("gender")
        age = data.get("age")

    # Собираем текст для проверки данных.
    output_text = (
        f"Пожалуйста проверьте правильность введённых данных\n"
        f"Имя: {name}\n"
        f"Пол: {gender}\n"
        f"Возраст: {age}\n"
        f"И либо сохраните введённые данные, либо отмените сохранение и введите данные заново"
    )
    return output_text
