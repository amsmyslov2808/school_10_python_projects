import random


def fill_array1(array1, count_items):
    for _ in range(count_items):
        array1.append(random.randint(1, 100))


array1 = []


def create_and_fill_array2(count_items):
    array = []
    for _ in range(count_items):
        array.append(random.randint(1, 100))

    return array


array2 = create_and_fill_array2(15)
