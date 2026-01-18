import random

my_collection = []

count_elems = 10

for _ in range(count_elems):
    my_collection.append(random.randint(1, 10))

print(my_collection)

# index = 3

# print(my_collection[index])

sum_elements = 0

for i in range(count_elems):
    if i % 2 == 1:
        sum_elements += my_collection[i]

print(sum_elements)
