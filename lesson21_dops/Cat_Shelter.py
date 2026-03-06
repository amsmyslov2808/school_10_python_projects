from Cat import Cat


class CatShelter:
    __name: str
    __address: str
    __contacts: str
    __cats: list[Cat]

    def __init__(self, name: str, address: str, contacts: str) -> None:
        self.__name = name
        self.__address = address
        self.__contacts = contacts
        self.__cats = []

    def add_cat(self, cat: Cat) -> None:
        self.__cats.append(cat)

    def print_info(self) -> None:
        print(f"Приют: {self.__name}")
        print(f"Адрес: {self.__address}")
        print(f"Контакты: {self.__contacts}")
        print(f"Количество котов: {len(self.__cats)}")
        print()
        print("Коты в приюте:")

        if not self.__cats:
            print("котов пока нет")
            return

        print("# | Имя | Возраст | Состояние")
        for index, cat in enumerate(self.__cats, start=1):
            status = "счастливый" if cat.get_is_happy() else "несчастный"
            print(f"{index} | {cat.get_name()} | {cat.get_age()} | {status}")
