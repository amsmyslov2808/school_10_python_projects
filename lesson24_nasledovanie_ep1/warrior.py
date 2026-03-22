from unit import Unit


class Warrior(Unit):
    __armor: int
    __stamina: int

    def __init__(
        self, hp: int, damage: int, type_name: str, armor: int, stamina: int
    ) -> None:
        super().__init__(hp, damage, type_name)
        self.__armor = armor
        self.__stamina = stamina

    def print_info(self) -> None:
        super().print_info()
        print(f"Броня: {self.__armor}")
        print(f"Выносливость: {self.__stamina}")

    def attack(self) -> int:
        print("attack in Warrior")
        damage = 0

        if self.__stamina > 0:
            damage = round((self._damage * self.__stamina) / 100)
            self.__stamina -= 10
        else:
            damage = 1

        return damage

    def take_damage(self, input_damage: int) -> None:
        print("take_damage in Warrior")
        if self.__armor > 0:
            self._hp = self._hp - (input_damage - self.__armor)
            self.__armor -= 1
        else:
            self._hp -= input_damage

        if self._hp < 0:
            self._hp = 0
