def get_screen_8_trip_info_text(trip: dict):
    note = trip["note"]

    if note == None:
        note = "Заметка о поездке отсутствует."

    return (
        f"Дата поездки: {trip['date']}\n"
        f"Название города: {trip['city']}\n\n"
        f"{note}"
    )
