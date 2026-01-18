number = int(input("введите число: "))

count_0 = 0
count_9 = 0
current_number = 0

while number != 0:
    current_number = number % 10
    number = number // 10

    if current_number == 0:
        count_0 = count_0 + 1

    if current_number == 9:
        count_9 = count_9 + 1

if count_0 > count_9:
    print("0 больше")
elif count_9 > count_0:
    print("9 больше")
else:
    print("количество 0 и 9 равно")
