my_collection_as_string = input("введите массив: ")

print(my_collection_as_string)

my_collection_as_items = my_collection_as_string.split()

print(my_collection_as_items)

my_collection = []

for i in range(len(my_collection_as_items)):
    my_collection.append(int(my_collection_as_items[i]))

print(my_collection)
