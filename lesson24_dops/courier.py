from decimal import Decimal


class Courier:
    _name: str
    _experience: int
    _rating: float
    _completed_orders: int
    _balance: Decimal
    _is_busy: bool

    def __init__(
        self,
        name: str,
        experience: int,
        rating: float,
        completed_orders: int,
        balance: Decimal,
        is_busy: bool,
    ):
        if len(name) == 0:
            raise ValueError("Name cannot be empty.")

        if experience < 0:
            raise ValueError("Experience cannot be negative.")

        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5.")

        if completed_orders < 0:
            raise ValueError("Completed orders cannot be negative.")

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self._name = name
        self._experience = experience
        self._rating = rating
        self._completed_orders = completed_orders
        self._balance = balance
        self._is_busy = is_busy

    def print_info(self) -> None:
        print(f"Name: {self._name}")
        print(f"Experience: {self._experience} months")
        print(f"Rating: {self._rating}")
        print(f"Completed Orders: {self._completed_orders}")
        print(f"Balance: ${self._balance:.2f}")
        print(f"Is Busy: {'Yes' if self._is_busy else 'No'}")

    def deliver_order(self, distance: float) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def _calculate_salary_for_order(self, distance: float) -> float:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def finish_shift(self) -> None:
        self._is_busy = False
        print("Shift finished.")
        print(f"Total orders completed: {self._completed_orders}")
        print(f"Final balance: ${self._balance:.2f}")
