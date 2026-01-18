# польз вводит символ и программа должна определить буква ли это
# если это не буква программа должна определить цифра ли это
# если это не буква и не цифра то программа долджна выдать что это неизвестный символ

symbol_as_str = input("введите символ: ")
symbol = symbol_as_str[0]

# print(ord(symbol))

# if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
#     print("это английская буква!")

#     if symbol >= "a" and symbol <= "z":
#         print("маленькая")
#     else:
#         print("большая")

# elif symbol >= "0" and symbol <= "9":
#     print("это цифра")

# else:
#     print("это неизвестный символ")


if symbol >= "a" and symbol <= "z":
    print("это английская буква! маленькая")

elif symbol >= "A" and symbol <= "Z":
    print("это английская буква! большая")

elif symbol >= "0" and symbol <= "9":
    print("это цифра")

else:
    print("это неизвестный символ")
