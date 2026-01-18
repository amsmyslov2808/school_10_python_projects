import random

my_collection = []

count_elements = 10

for _ in range(count_elements):
    my_collection.append(random.randint(1, 100))

for i in range(count_elements):  # 0 1 2 3 4 .. 9
    # if my_collection[i] % 2 == 0:
    #     print(f"{i}: {my_collection[i]}")
    print(f"{i}: {my_collection[i]}")

my_collection[0] = 999
my_collection[count_elements - 1] = 333

print(my_collection)

print(my_collection[1])

my_collection.pop(1)
# my_collection.clear()

print(my_collection)

my_collection.insert(1, 777)

print(my_collection)
