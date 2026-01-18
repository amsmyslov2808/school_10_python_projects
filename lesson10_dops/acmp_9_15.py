word = input("введите слово: ")
k = int(input("введите номер буквы которую вы хотите вывести: ")) - 1

if k >= 0 and k < len(word):
    print(word[k])
else:
    print("такой буквы нет")
