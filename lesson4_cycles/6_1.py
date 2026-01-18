current_number = 0
sum_numbers = 0
count_numbers = 0
asnwer = ""
is_run = True

while is_run == True:
    current_number = int(input("введите очередное число в последовательности: "))

    if current_number != 999:
        sum_numbers = sum_numbers + current_number
        count_numbers = count_numbers + 1
    else:  # ==999
        asnwer = input("вы хотите добавить это число к числовому ряду (y/n)?: ")
        if asnwer == "y":
            sum_numbers = sum_numbers + current_number
            count_numbers = count_numbers + 1
        else:
            is_run = False

print(f"всего введено чисел = {count_numbers}")
print(f"сумма всех чисел = {sum_numbers}")
