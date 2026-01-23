file_in = open("INPUT.txt", "r", encoding="utf-8")
file_out = open("OUTPUT.txt", "w", encoding="utf-8")

data = file_in.readline()

first_space = data.find(" ")

k = int(data[0:first_space]) - 1
s = data[first_space:].strip()

result = s[:k] + s[k + 1 :]

file_out.write(result)

file_in.close()
file_out.close()
