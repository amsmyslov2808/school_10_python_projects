from cinema import Cinema
from session import Session
from movie import Movie
from datetime import datetime
from decimal import Decimal
import console_services

cinema: Cinema = Cinema("Cinema 1")
cinema.add_session(
    Session(Movie("Movie 1", 120, 16), datetime(2005, 7, 14, 12, 30), Decimal(300), 100)
)

while True:
    console_services.clear_console()

    print("Выберите действие")
    print("1. Показать все сеансы")
    print("2. Посмотреть свободные места на сеансе")
    print("5. Выход")

    action = console_services.input_int("введите число от 1 до 5: ", 1, 5)

    if action == 1:
        print("Сеансы в кинотеатре:")
        for current_session in cinema.show_sessions():
            print(current_session)
    elif action == 2:
        pass
    elif action == 3:
        pass
