import random

my_collection = []
temp = 0
count_numbers = int(input("введите кол-во элементов коллекции: "))

for _ in range(count_numbers):
    my_collection.append(random.randint(1, 100))

print(my_collection)

for i in range(0, count_numbers, 2):
    temp = my_collection[i]
    my_collection[i] = my_collection[i + 1]
    my_collection[i + 1] = temp


print(my_collection)
