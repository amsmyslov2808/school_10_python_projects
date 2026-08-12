from models.holliday import Holiday


def get_screen_3_holidays_text(holidays: list[Holiday]):
    if len(holidays) == 0:
        return (
            "К сожалению, ни одного праздника не найдено. "
            "Рекомендуем придумать себе праздник самостоятельно."
        )

    output_text = "Праздники на ближайшие 30 дней\n\n"

    for holiday_number, holiday in enumerate(holidays, start=1):
        holiday_description = (
            f"Страна: {holiday.country}. "
            f"Тип праздника: {holiday.type_to_str()}."
        )
        output_text += (
            f"{holiday_number}. {holiday.name} — {holiday.date_to_str()}\n"
            f"{holiday_description}\n\n"
        )

    return output_text.strip()


def get_screen_4_city_input_text():
    return "Введите название города, в котором Вы сейчас находитесь."


def get_screen_7_trips_text():
    return (
        "Список городов\n\n"
        "1. 10.08.2026 — Москва\n\n"
        "2. 03.08.2026 — Калуга\n\n"
        "3. 25.07.2026 — Орёл\n\n"
        "4. 18.07.2026 — Тула\n\n"
        "5. 11.07.2026 — Рязань"
    )
