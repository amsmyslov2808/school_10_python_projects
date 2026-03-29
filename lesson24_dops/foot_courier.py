from decimal import Decimal

from courier import Courier


class FootCourier(Courier):
    __max_distance: float
    __speed: float

    def __init__(
        self,
        name: str,
        experience: int,
        rating: float,
        completed_orders: int,
        balance: Decimal,
        is_busy: bool,
        max_distance: float,
        speed: float,
    ):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)

        if max_distance < 0:
            raise ValueError("Max distance must be positive.")

        if speed < 0:
            raise ValueError("Speed must be positive.")

        self.__max_distance = max_distance
        self.__speed = speed

    def print_info(self) -> None:
        super().print_info()
        print(f"Max Distance: {self.__max_distance} km")
        print(f"Speed: {self.__speed} km/h")

    def _calculate_salary_for_order(self, distance: float) -> float:
        base_rate = 25.0
        fix_price = 120.0
        return base_rate * distance + fix_price

    def deliver_order(self, distance: float) -> None:
        if distance > self.__max_distance:
            raise ValueError(
                f"Distance {distance} km exceeds max distance of {self.__max_distance} km."
            )

        self._completed_orders += 1
        salary = self._calculate_salary_for_order(distance)
        self._balance += Decimal(salary)
        print(f"Delivered order for {distance} km. Earned ${salary:.2f}.")
