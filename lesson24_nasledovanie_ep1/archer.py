from unit import Unit


class Archer(Unit):
    __count_arrows: int

    def __init__(self, hp: int, damage: int, type_name: str, count_arrows: int) -> None:
        super().__init__(hp, damage, type_name)
        self.__count_arrows = count_arrows

    def print_info(self) -> None:
        super().print_info()
        print(f"Количество стрел: {self.__count_arrows}")

    def attack(self) -> int:
        print("attack in Archer")

        damage = 0

        if self.__count_arrows > 0:
            self.__count_arrows -= 1
            damage = self._damage
        else:
            damage = self._damage // 2

        return damage

    def take_damage(self, input_damage: int) -> None:
        print("take_damage in Archer")
        self._hp -= input_damage
        if self._hp < 0:
            self._hp = 0
