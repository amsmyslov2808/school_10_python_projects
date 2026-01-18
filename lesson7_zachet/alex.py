import random

a = []
temp = 0
count_numbers = int(input("введите кол-во элементов массива: "))

for _ in range(count_numbers):
    a.append(random.randint(1, 100))

print(a)

for i in range(count_numbers // 2):
    temp = a[i]
    a[i] = a[count_numbers - 1 - i]
    a[count_numbers - 1 - i] = temp

print(a)
