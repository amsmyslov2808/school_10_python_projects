file_in = open("stih.txt", encoding="utf-8")

data = file_in.read()

count_a = 0

for item in data:
    if item == "а":
        count_a += 1

file_out = open("result.txt", "w")

percent_a = count_a / len(data) * 100
percent_a_str = f"{percent_a:.2f}%"

file_out.write(percent_a_str)

file_in.close()
file_out.close()
