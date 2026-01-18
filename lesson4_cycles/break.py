is_complex = False
number = 100

for devider in range(2, number):  # 2 3 4 5 6 7 ... 99
    if number % devider == 0:
        is_complex = True
        break

if is_complex == True:
    print(f"число {number} составное")
else:
    print(f"число {number} простое")
