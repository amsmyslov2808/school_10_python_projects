from BankCard import BankCard


class CardsStorage:
    __cards: list[BankCard]

    def __init__(self) -> None:
        self.__cards = []

    def add_new_card(self, card: BankCard) -> None:
        self.__cards.append(card)

    def print_all_cards(self) -> None:
        for item in self.__cards:
            print(item.get_info())

    def __get_card_by_card_number(self, card_number: int) -> BankCard | None:
        for item in self.__cards:
            if item.get_card_number() == card_number:
                return item

        return None

    def transfer_from_card_to_card(
        self, card_number_from: int, card_number_to: int, transfer_money: int
    ) -> None:
        card_from = self.__get_card_by_card_number(card_number_from)
        if card_from == None:
            print(f"Error. Карта с номером {card_number_from} не найдена")
            return

        card_to = self.__get_card_by_card_number(card_number_to)
        if card_to == None:
            print(f"Error. Карта с номером {card_number_from} не найдена")
            return

        if card_from.get_balance() < transfer_money:
            print(f"Error. На карте с номером {card_number_from} не хватает")
            return

        card_from.withdraw_money(transfer_money)

        card_to.add_money(transfer_money)
