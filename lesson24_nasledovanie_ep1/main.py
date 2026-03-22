# from unit import Unit
from archer import Archer
from warrior import Warrior

archer: Archer = Archer(10, 5, "Лучник", 8)
warrior: Warrior = Warrior(10, 5, "Воин", 4, 100)

archer.print_info()
print("*" * 15)
warrior.print_info()

print("*" * 15)
print("*" * 15)

warrior.take_damage(archer.attack())

archer.print_info()
print("*" * 15)
warrior.print_info()

print("*" * 15)
print("*" * 15)

warrior.take_damage(archer.attack())

archer.print_info()
print("*" * 15)
warrior.print_info()

print("*" * 15)
print("*" * 15)

archer.take_damage(warrior.attack())

archer.print_info()
print("*" * 15)
warrior.print_info()

print("*" * 15)
print("*" * 15)

archer.take_damage(warrior.attack())

archer.print_info()
print("*" * 15)
warrior.print_info()

print("*" * 15)
print("*" * 15)

archer.take_damage(warrior.attack())

archer.print_info()
print("*" * 15)
warrior.print_info()

print(archer.is_alive())
print(warrior.is_alive())
