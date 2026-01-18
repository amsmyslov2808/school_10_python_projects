word = ""
word = input("введите любое слово: ")


indx_first = word.find("е")
indx_last = word.rfind("е")

if indx_first != -1:
    print(f"первая е содержит индекс:{indx_first+1} ")
else:
    print("первой буквы е нет в слове")

if indx_last != -1:
    print(f"последняя с начала е содержит индекс:{indx_last+1} ")
    print(f"с конца: {len(word)-indx_last}")
else:
    print("последней буквы е нет в слове")
