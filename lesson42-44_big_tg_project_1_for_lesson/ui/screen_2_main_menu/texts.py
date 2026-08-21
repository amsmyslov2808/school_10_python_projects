"""Текстовые заглушки для разделов, доступных из главного меню."""

from models.holliday import Holiday


def get_screen_3_holidays_text(holidays: list[Holiday]):
    """Формирует текст списка праздников для экрана 3."""

    # API может вернуть пустой список, например если праздников не нашлось.
    if len(holidays) == 0:
        return (
            "К сожалению, ни одного праздника не найдено. "
            "Рекомендуем придумать себе праздник самостоятельно."
        )

    # В эту строку последовательно добавляется информация о каждом празднике.
    output_text = "Праздники на ближайшие 7 дней\n\n"

    # enumerate нумерует праздники начиная с 1, а не с 0.
    for holiday_number, holiday in enumerate(holidays, start=1):
        holiday_description = (
            f"Страна: {holiday.country}. "
            f"Тип праздника: {holiday.type_to_str()}."
        )
        output_text += (
            f"{holiday_number}. {holiday.name} — {holiday.date_to_str()}\n"
            f"{holiday_description}\n\n"
        )

    # Убираем последние два перевода строки после последнего праздника.
    return output_text.strip()


def get_screen_4_city_input_text():
    """Возвращает приглашение перейти к вводу исходного города."""
    return "Введите название города, в котором Вы сейчас находитесь."


def get_screen_7_trips_text():
    """Возвращает текст экрана с историей поездок пользователя."""
    return (
        "Список городов\n\n"
        "1. 10.08.2026 — Москва\n\n"
        "2. 03.08.2026 — Калуга\n\n"
        "3. 25.07.2026 — Орёл\n\n"
        "4. 18.07.2026 — Тула\n\n"
        "5. 11.07.2026 — Рязань"
    )
