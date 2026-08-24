def get_screen_8_trip_info_text(trip):
    """Формирует подробную информацию об одной поездке."""

    note = trip.note
    if note == "" or note is None:
        note = "Заметка о поездке отсутствует."

    trip_date = trip.arrival_date.strftime("%d.%m.%Y %H:%M")
    return (
        f"Дата поездки: {trip_date}\n"
        f"Город: {trip.name}\n\n"
        f"Заметка:\n{note}"
    )
