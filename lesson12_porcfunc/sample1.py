def input_number(message):
    is_good_number = False
    number = 0

    while is_good_number == False:
        temp = input(message)

        if temp.isdigit() == True:
            number = int(temp)
            is_good_number = True
        else:
            print("Ошибка. Вы ввели не число")

    return number


def sum_numbers(a, b):
    return a + b


def print_result(result):
    print(f"сумма = {result}")


a = input_number("введите первое число: ")
b = input_number("введите второе число: ")

result = sum_numbers(a, b)

print_result(result)
