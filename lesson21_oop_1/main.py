from BankCard import BankCard
from CardsStorage import CardsStorage

cardsStorage = CardsStorage()

cardsStorage.add_new_card(BankCard("Alexey Smyslov", 4388012345678910, 1000))
cardsStorage.add_new_card(BankCard("Ildar Martiyanov", 4388012345678911, 1500))

cardsStorage.print_all_cards()

cardsStorage.transfer_from_card_to_card(4388012345678911, 4388012345678910, 1500)

cardsStorage.print_all_cards()
