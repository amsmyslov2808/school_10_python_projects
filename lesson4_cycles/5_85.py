number = 83764
current_digit = 0
reverse_number = 0

while number != 0:
    current_digit = number % 10
    number = number // 10
    reverse_number = reverse_number * 10 + current_digit

print(reverse_number)
