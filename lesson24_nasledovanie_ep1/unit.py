class Unit:
    _hp: int
    _damage: int
    _type_name: str

    def __init__(self, hp: int, damage: int, type_name: str) -> None:
        self._hp = hp
        self._damage = damage
        self._type_name = type_name

    def print_info(self) -> None:
        print(self._type_name)
        print(f"Здоровье: {self._hp}")
        print(f"Урон: {self._damage}")

    def is_alive(self) -> bool:
        return self._hp > 0

    def attack(self) -> int:
        raise NotImplementedError("метод attack не определён в текущем классе")

    def take_damage(self, input_damage: int) -> None:
        raise NotImplementedError("метод take_damage не определён в текущем классе")
