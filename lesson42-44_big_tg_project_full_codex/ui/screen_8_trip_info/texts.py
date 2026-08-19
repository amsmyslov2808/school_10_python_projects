def get_screen_8_trip_info_text(trip):
    """Формирует подробную информацию об одной поездке."""

    note = trip.note if trip.note else "Заметка о поездке отсутствует."
    return f"Дата поездки: {trip.arrival_date.strftime('%d.%m.%Y %H:%M')}\nГород: {trip.name}\n\nЗаметка:\n{note}"
