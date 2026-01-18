file = open("input_15_8.txt", "r", encoding="utf-8")

file_data = file.read()

count_letters = len(file_data.replace("\n", ""))
# count_letters = 0

# for i in file_data:
#     if i != "\n":
#         count_letters += 1

print(f"count_letters = {count_letters}")

# count_symbols = len(file_data)

file.close()

# print(f"count_lines = {count_symbols}")
