file = open("input_15_8.txt", "r", encoding="utf-8")


for line in file:
    line = line.rstrip("\n")

    count_symbols = len(line)

    if count_symbols != 0:
        print(count_symbols)

file.close()
