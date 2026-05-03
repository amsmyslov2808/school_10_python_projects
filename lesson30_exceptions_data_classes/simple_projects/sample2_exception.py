# import sys

# try:
#     a = int(input("a: "))
# except ValueError:
#     print("Ошибка. Вы ввели не число")
#     sys.exit(0)

a = 0
b = 0
res = 0

is_correct_input = False
while is_correct_input == False:
    try:
        a = int(input("a: "))
        is_correct_input = True
    except ValueError as e:
        print(f"Ошибка. Вы ввели не число. Техническая информация: {e}")


is_correct_input = False
while is_correct_input == False:
    try:
        b = int(input("b: "))
        is_correct_input = True
    except ValueError as e:
        print(f"Ошибка. Вы ввели не число. Техническая информация: {e}")


# try:
#     b = int(input("b: "))
# except ValueError:
#     print("Ошибка. Вы ввели не число")

# try:
#     res = a / b
#     print(f"res = {res}")
# except ZeroDivisionError:
#     print("Ошибка. Делить на 0 нельзя")

try:
    res = a / b
except ZeroDivisionError as e:
    print(f"Ошибка. Делить на 0 нельзя. Техническая информация: {e}")
else:
    print(f"res = {res}")
