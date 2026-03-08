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

    __MIN_DECREASE = 1
    __MAX_DECREASE = 3

    __EVENT_CHANCE = 30

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
        increase_energy = random.randint(self.__MIN_INCREASE, self.__MAX_ICREASE)

        self.__energy_level += increase_energy

        if self.__energy_level > self.__MAX_LEVEL:
            self.__energy_level = self.__MAX_LEVEL

            print(
                f"{self.__name} переел. его уровень энергии достиг максимума. его здоровье ухудшается на 1 пункт"
            )

            self.__health_level -= 1

        increase_health = random.randint(self.__MIN_INCREASE, self.__MAX_ICREASE - 1)

        self.__health_level += increase_health

    def play(self) -> None:
        increase_happiness = random.randint(self.__MIN_INCREASE, self.__MAX_ICREASE)

        self.__happiness_level += increase_happiness

        if self.__happiness_level > self.__MAX_LEVEL:
            self.__happiness_level = self.__MAX_LEVEL

            print(
                f"{self.__name} слишком много играл. его уровень счастья достиг максимума."
            )

        decrease_energy = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)

        self.__energy_level -= decrease_energy

        event_percent = random.randint(1, 100)
        if 1 <= event_percent <= self.__EVENT_CHANCE:

            decrease_health = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)

            print(
                f"{self.__name} поранился во время игры. его здоровье ухудшается на {decrease_health} пунктов."
            )

            self.__health_level -= decrease_health

    def sleep(self) -> None:
        increase_energy = random.randint(
            self.__MIN_INCREASE + 2, self.__MAX_ICREASE + 3
        )

        self.__energy_level += increase_energy

        if self.__energy_level > self.__MAX_LEVEL:
            self.__energy_level = self.__MAX_LEVEL

            print(
                f"{self.__name} слишком много спал. его уровень энергии достиг максимума."
            )

        increase_health = random.randint(self.__MIN_INCREASE, self.__MAX_ICREASE - 1)

        self.__health_level += increase_health

        decrease_happiness = random.randint(
            self.__MIN_DECREASE, self.__MAX_DECREASE - 1
        )

        self.__happiness_level -= decrease_happiness

    def random_event(self) -> None:
        event_percent = random.randint(1, 100)
        if 1 <= event_percent <= self.__EVENT_CHANCE:
            event_number = random.randint(1, 3)

            decrease = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)

            if event_number == 1:
                self.__health_level -= decrease

                print(
                    f"{self.__name} съел протухшую вкусняшку и его здоровье уменьшилось на {decrease}."
                )

            elif event_number == 2:
                self.__happiness_level -= decrease

                print(
                    f"{self.__name} поссорился с другим тамагочи и его счастье уменьшилось на {decrease}."
                )

            elif event_number == 3:
                self.__energy_level -= decrease

                print(
                    f"{self.__name} посмотрел грустный фильм и его энергия уменьшилась на {decrease}."
                )

    def check_health(self) -> None:
        if self.__energy_level <= self.__MIN_LEVEL:
            print(f"{self.__name} слишком устал и его здоровье ухудшается на 1 пункт.")
            self.__health_level -= 1

        if self.__happiness_level <= self.__MIN_LEVEL:
            print(
                f"{self.__name} слишком грустный и его здоровье ухудшается на 1 пункт."
            )
            self.__health_level -= 1

    def print_status(self) -> None:
        def format_level(level: int) -> str:
            left_scale = ""
            right_scale = ""

            if level > self.__MIN_LEVEL:
                left_scale = "□" * self.__MAX_LEVEL
                right_scale = "■" * level + "□" * (self.__MAX_LEVEL - level)

            elif level < self.__MIN_LEVEL:
                left_scale = "□" * (self.__MAX_LEVEL - level) + "■" * level
                right_scale = "□" * self.__MAX_LEVEL

            elif level == self.__MIN_LEVEL:
                left_scale = "□" * self.__MAX_LEVEL
                right_scale = "□" * self.__MAX_LEVEL

            return f"[{left_scale}]|[{right_scale}] ({level:+d})"

        print(
            f"Имя: {self.__name}\n"
            f"Вид животного: {self.__type_animal}\n"
            f"Возраст: {self.__age}\n"
            f"Уровень здоровья: {format_level(self.__health_level)}\n"
            f"Уровень счастья: {format_level(self.__happiness_level)}\n"
            f"Уровень энергии: {format_level(self.__energy_level)}"
        )
