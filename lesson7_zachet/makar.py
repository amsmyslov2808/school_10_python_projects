first_number = int(input("введите первое число: "))
second_number = int(input("введите второе число: "))
third_number = int(input("введите третье число: "))

min_num = first_number

if second_number < min_num:
    min_num = second_number

if third_number < min_num:
    min_num = third_number

print(f"минимальное число = {min_num}")
