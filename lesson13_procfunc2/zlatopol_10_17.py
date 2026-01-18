def fact(number):
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


result = (2 * fact(5) + 3 * fact(8)) / (fact(6) + fact(4))

print(f"результат = {result:.2f}")
