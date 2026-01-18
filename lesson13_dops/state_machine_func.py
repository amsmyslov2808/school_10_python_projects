def input_int(message):
    is_correct_input = False
    number = 0

    while is_correct_input == False:
        try:
            number = int(input(f"{message}"))
            is_correct_input = True
        except:
            print("Ошибка. Вы ввели НЕ число")

    return number
