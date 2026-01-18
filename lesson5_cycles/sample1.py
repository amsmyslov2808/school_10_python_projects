import math

x = int(input("введите Х: "))
y = int(input("введите Y: "))

xx = x
yy = y

koef = 1
if x < 0:
    koef = koef * -1

if y < 0:
    koef = koef * -1

x = abs(x)
y = abs(y)

i = 0
sum = 0

# while i < y:
#     i = i + 1
#     sum = sum + x

# while i < x:
#     i = i + 1
#     sum = sum + y

for _ in range(y):
    sum = sum + x

# for _ in range(x):
#     sum = sum + y

sum = sum * koef

print(f"{xx} * {yy} = {sum}")
