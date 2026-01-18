# print(*range(5))

# for _ in range(5):
#     print("hello")

# for i in range(1, 9 + 1):
#     print(f"{i} x 7 = {i*7}")

a = int(input("введите a: "))

b = a - 1

while b < a:
    b = int(input("введите b: "))

    if b < a:
        print("Ошибка. b должн быть >= a")

sum = 0

for i in range(a, b + 1):
    sum = sum + i

print(f"сумма чисел от {a} до {b} = {sum}")
