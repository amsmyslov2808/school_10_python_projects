import math


def is_simple(number):
    if number <= 0:
        return False

    if number == 1 or number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)), 2):
        if number % i == 0:
            return False

    return True


for number in range(100, 999 + 1):
    if is_simple(number) == True:
        print(number)
