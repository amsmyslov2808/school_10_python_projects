result = 0
is_correct_input = False

while is_correct_input == False:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        result = a / b
        is_correct_input = True
    except:
        print("ошибка при вводе или расчётах. повторите ввод ещё раз")
        is_correct_input = False


print(f"result = {result}")
