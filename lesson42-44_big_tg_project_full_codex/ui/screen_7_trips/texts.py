def get_screen_7_trips_text(trips, page: int):
    """Формирует страницу истории поездок."""

    if len(trips) == 0:
        return "История поездок пока пуста. Выберите город для своей первой поездки."

    output_text = "История поездок\n\n"
    for trip_number, trip in enumerate(trips, start=1):
        output_text += f"{trip_number}. {trip.arrival_date.strftime('%d.%m.%Y')} — {trip.name}\n\n"
    return output_text.strip()
