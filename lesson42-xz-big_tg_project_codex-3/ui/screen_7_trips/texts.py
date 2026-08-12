MOCK_TRIPS = [
    {"date": "10.08.2026", "city": "Москва", "note": None},
    {"date": "03.08.2026", "city": "Калуга", "note": "Гуляли по центру города."},
    {"date": "25.07.2026", "city": "Орёл", "note": None},
    {"date": "18.07.2026", "city": "Тула", "note": "Купили тульский пряник."},
    {"date": "11.07.2026", "city": "Рязань", "note": None},
    {"date": "04.07.2026", "city": "Коломна", "note": "Посетили кремль."},
    {"date": "28.06.2026", "city": "Суздаль", "note": None},
    {"date": "21.06.2026", "city": "Владимир", "note": "Посмотрели Золотые ворота."},
    {"date": "14.06.2026", "city": "Ярославль", "note": None},
    {"date": "07.06.2026", "city": "Кострома", "note": "Гуляли по набережной Волги."},
    {"date": "31.05.2026", "city": "Тверь", "note": None},
    {"date": "24.05.2026", "city": "Серпухов", "note": "Посетили Высоцкий монастырь."},
    {"date": "17.05.2026", "city": "Звенигород", "note": None},
    {"date": "10.05.2026", "city": "Дмитров", "note": "Хорошо провели выходной."},
]


def get_screen_7_trips_text(trips: list[dict], page: int, total_pages: int):
    output_text = "Список городов\n\n"

    for trip_number, trip in enumerate(trips, start=1):
        output_text += (
            f"{trip_number}. {trip['date']} — {trip['city']}\n\n"
        )

    output_text += f"Страница {page + 1}/{total_pages}"
    return output_text
