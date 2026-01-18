ticket = 0
left_part = 0
right_part = 0

digit1 = 0
digit2 = 0
digit3 = 0

sum_left = 0
sum_right = 0

ticket = int(input("введите номер билета: "))

left_part = ticket // 1000
right_part = ticket % 1000

digit1 = left_part // 100
digit2 = (left_part % 100) // 10
digit3 = left_part % 10

sum_left = digit1 + digit2 + digit3  # находим сумму цифр левой части

digit1 = right_part // 100
digit2 = (right_part % 100) // 10
digit3 = right_part % 10

sum_right = digit1 + digit2 + digit3  # находим сумму цифр правой части

# print(f"sum_left = {sum_left} sum_right = {sum_right}")

if sum_left == sum_right:
    print("Поздравляем ваш билет счастливый")
else:
    print("Сорри не повезло, билет несчастливый")
