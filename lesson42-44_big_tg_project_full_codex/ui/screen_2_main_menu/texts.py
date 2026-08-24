"""Текстовые заглушки для разделов, доступных из главного меню."""

from models.holliday import Holiday


def get_screen_3_holidays_text(holidays: list[Holiday]):
    """Формирует текст списка праздников для экрана 3."""

    if len(holidays) == 0:
        return (
            "К сожалению, ни одного праздника не найдено. "
            "Рекомендуем придумать себе праздник самостоятельно."
        )

    output_text = "Праздники на ближайшие 30 дней\n\n"

    for i in range(0, len(holidays)):
        output_text += f"{i + 1}. {holidays[i].name} — {holidays[i].date_to_str()}\n"
        output_text += f"Страна: {holidays[i].country}. "
        output_text += f"Тип праздника: {holidays[i].type_to_str()}.\n\n"

    return output_text


def get_screen_4_city_input_text():
    """Возвращает приглашение перейти к вводу исходного города."""
    return "Введите название города, в котором Вы сейчас находитесь."


def get_screen_7_trips_text(trips):
    """Формирует текст экрана с историей поездок пользователя."""

    if len(trips) == 0:
        return "История поездок пока пуста. Выберите город для своей первой поездки."

    output_text = "История поездок\n\n"

    for i in range(0, len(trips)):
        trip_date = trips[i].arrival_date.strftime("%d.%m.%Y")
        output_text += f"{i + 1}. {trip_date} — {trips[i].name}\n\n"

    return output_text
