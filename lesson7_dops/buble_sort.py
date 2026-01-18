a = list([int(x) for x in input().split()])
for j in range(len(a)):
    for i in range(0, len(a) - 1 - j):
        if a[i + 1] < a[i]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)

import random

my_collection = []
count_elems = 5

is_sort = False
temp = 0
offset = 0

for _ in range(count_elems):
    my_collection.append(random.randint(1, 100))

print(my_collection)

while is_sort == False:
    is_sort = True

    for i in range(count_elems - 1 - offset):
        if my_collection[i + 1] < my_collection[i]:
            temp = my_collection[i]
            my_collection[i] = my_collection[i + 1]
            my_collection[i + 1] = temp
            is_sort = False

    offset += 1

print()
print(my_collection)
