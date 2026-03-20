from movie import Movie
from datetime import datetime
from decimal import Decimal


class Session:
    __movie: Movie
    __session_datetime: datetime
    __price: Decimal
    __number_of_seats: int
    __occupied_places: list[int]

    def __init__(
        self,
        movie: Movie,
        session_datetime: datetime,
        price: Decimal,
        number_of_seats: int,
    ):
        self.__movie = movie
        self.__session_datetime = session_datetime
        self.__price = price
        self.__number_of_seats = number_of_seats
        self.__occupied_places = []

    def show_free_seats(self) -> list[int]:
        empty_places: list[int] = []

        for current_number in range(1, self.__number_of_seats + 1):
            if current_number not in self.__occupied_places:
                empty_places.append(current_number)

        return empty_places

    def book_seat(self, seat_number: int) -> None:
        pass

    def cancel_booking(self, seat_number: int) -> None:
        pass

    def get_info(self) -> str:
        return f"{self.__movie.get_info()} - {self.__session_datetime.strftime('%Y-%m-%d %H:%M')} - {self.__price} руб."
