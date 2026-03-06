class Cat:
    __name: str
    __age: int
    __is_happy: bool

    def __init__(self, name: str, age: int, is_happy: bool) -> None:
        self.__name = name
        self.__age = age
        self.__is_happy = is_happy

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_is_happy(self) -> bool:
        return self.__is_happy

    def get_info(self) -> str:
        return f"Кот по имени {self.__name}, возраст {self.__age} лет, {'счастливый' if self.__is_happy else 'несчастный'}"

    def growing_up(self) -> None:
        self.__age += 1

    def set_is_happy(self, is_happy: bool) -> None:
        self.__is_happy = is_happy

    def make_happy(self) -> None:
        self.__is_happy = True

    def make_unhappy(self) -> None:
        self.__is_happy = False
