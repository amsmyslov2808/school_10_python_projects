my_collections = [3, 4, 6, 7, 8, 4, 23]

print(my_collections)

my_collections[0] = 323
print(my_collections[0])

print(my_collections)

for i in range(len(my_collections)):
    # print(my_collections[i], end=" ")
    my_collections[i] *= 2

print(my_collections)

my_collections2 = []
for item in my_collections:
    my_collections2.append(item * 2)

print(my_collections2)
