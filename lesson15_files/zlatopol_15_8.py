file = open("input_15_8.txt", "r", encoding="utf-8")

# count_lines = 0
# for line in file:
#     count_lines += 1

# print(file.read().split("\n"))

count_lines = len(file.readlines())

file.close()

print(f"count_lines = {count_lines}")
