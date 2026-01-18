# def print_hello(count_repeats):
#     for _ in range(count_repeats):
#         print("hello")


# print_hello(3)


# def is_simple(number):
#     if number <= 0:
#         return False

#     if number == 1 or number == 2:
#         return True

#     if number % 2 == 0:
#         return False

#     for i in range(3, number, 2):
#         if number % i == 0:
#             return False

#     return True


# for number in range(1, 20 + 1):
#     if is_simple(number) == True:
#         print(number)


def fact(number):
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


result = (fact(2) + fact(5)) / fact(7)


print(f"результат выражения = {result}")
