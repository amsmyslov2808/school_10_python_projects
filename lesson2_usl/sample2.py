month_number = 0

while month_number < 1 or month_number > 12:
    month_number = int(input("введите номер месяца: "))

    if month_number < 1 or month_number > 12:
        print("Ошибка. Номер месяца должен быть от 1 до 12")


if month_number == 1:
    print("январь")
elif month_number == 2:
    print("февраль")
