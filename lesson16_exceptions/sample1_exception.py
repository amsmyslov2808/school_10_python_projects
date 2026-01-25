def input_int(min_number, max_number):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = int(input("введите число: "))

            if number < min_number or number > max_number:
                print(
                    f"ошибка ввода. число должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


number = input_int(10, 100)
print(f"введённое число: {number}")
