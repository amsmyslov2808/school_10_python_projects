import math

number = 0

while number <= 0:
    number = float(input("ввеедите число для извлечение квадратного корня: "))

    if number <= 0:
        print("Ошибка. Вы ввели число <= 0")

result = math.sqrt(number)

print(f"квадратный корень из числа {number} = {result}")
