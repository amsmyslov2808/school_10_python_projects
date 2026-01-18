import math


# реализация
def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# алгоритм
x1 = 2
y1 = 3

x2 = 5
y2 = 6

x3 = 10
y3 = 3

perimetr = (
    get_distance(x1, y1, x2, y2)
    + get_distance(x2, y2, x3, y3)
    + get_distance(x1, y1, x3, y3)
)

print(f"периметр треугольника = {perimetr:.2f}")
