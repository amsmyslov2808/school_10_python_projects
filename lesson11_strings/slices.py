stroka = "мама мыла раму"

start = 0
finish = 4

reverse_mama = stroka[3::-1]
mama = stroka[0:4]
mila_ramu = stroka[5::-1]
# mila_ramu = stroka[5:]
# new_stroka = stroka[::]
new_stroka = stroka[::-1]
# new_new_stroka = stroka[1:6:2]
# new_new_stroka = stroka[1:6:2]
new_new_stroka = stroka[5:0:-2]

# stroka_result = stroka[:4] + "_" + stroka[10:]
stroka_result = stroka[:4] + "_" + stroka[-4:]

print(stroka_result)
print(reverse_mama)
print(mama)
print(mila_ramu)
print(new_stroka)
print(new_new_stroka)


# stroka_as_list = list(stroka)

# print(stroka_as_list)

# stroka_from_list = "".join(stroka_as_list)

# print(stroka_from_list)
