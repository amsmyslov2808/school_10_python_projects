class BankCard:
    __owner_name: str
    __card_number: int
    __balance: int

    def __init__(self, owner_name: str, card_number: int, balance: int) -> None:
        if balance < 0:
            balance = 0

        if card_number < 1_000_000_000_000_000:
            card_number = 1_000_000_000_000_000

        if len(owner_name) < 2:
            owner_name = "Anonymous"

        self.__owner_name = owner_name
        self.__card_number = card_number
        self.__balance = balance

    def get_owner_name(self) -> str:
        return self.__owner_name

    def get_card_number(self) -> int:
        return self.__card_number

    def get_balance(self) -> int:
        return self.__balance

    def set_balance(self, new_balance: int) -> None:
        if new_balance >= 0 and new_balance <= 1_000_000:
            self.__balance = new_balance
        else:
            print("Error. Balance must be in range [0; 1000000]")

    def add_money(self, money: int) -> None:
        if money >= 0 and money <= 100_000:
            self.__balance += money
        else:
            print("Error. Money must be in range [0; 100000]")

    def withdraw_money(self, money: int) -> None:
        if money >= 0 and money <= 100_000:
            self.__balance -= money
        else:
            print("Error. Money must be in range [0; 100000]")

    def get_info(self) -> str:
        return f"Owner: {self.__owner_name}, Card number: {self.__card_number}, Balance: {self.__balance}"
