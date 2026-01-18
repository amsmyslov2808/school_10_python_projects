prime_number = 9139

number = prime_number

first_number = 0
current_number = 0
counter = 0

while number != 0:
    first_number = number % 10
    number = number // 10

number = prime_number

while number != 0:
    current_number = number % 10
    number = number // 10

    if current_number == first_number:
        counter = counter + 1

print(counter)
