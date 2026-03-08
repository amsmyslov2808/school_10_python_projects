import random


class Tamagotchi:
    __name: str
    __type_animal: str
    __age: int
    __health_level: int
    __happiness_level: int
    __energy_level: int

    __MIN_LEVEL = 0
    __MAX_LEVEL = 10

    def __init__(self, name: str, type_animal: str, age: int):
        self.__name = name
        self.__type_animal = type_animal
        self.__age = age
        self.__health_level = random.randint(self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3)
        self.__happiness_level = random.randint(
            self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3
        )
        self.__energy_level = random.randint(self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3)
