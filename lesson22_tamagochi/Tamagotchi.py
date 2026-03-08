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

    __MIN_INCREASE = 1
    __MAX_ICREASE = 3

    def __init__(self, name: str, type_animal: str, age: int):
        self.__name = name
        self.__type_animal = type_animal
        self.__age = age
        self.__health_level = random.randint(self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3)
        self.__happiness_level = random.randint(
            self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3
        )
        self.__energy_level = random.randint(self.__MIN_LEVEL + 5, self.__MAX_LEVEL - 3)

    def is_alive(self) -> bool:
        return self.__health_level > self.__MIN_LEVEL

    def feed(self) -> None:
        increase = random.randint(self.__MIN_INCREASE, self.__MAX_ICREASE)

        self.__energy_level = self.__energy_level + increase

        if self.__energy_level > self.__MAX_LEVEL:
            self.__energy_level = self.__MAX_LEVEL

            print(
                f"{self.__name} переел. его уровень энергии достиг максимума. его здоровье ухудшается на 1 пункт"
            )

            self.__health_level = self.__health_level - 1
