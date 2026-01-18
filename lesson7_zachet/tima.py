final_number = int(input("введите финальное число: "))

for i in range(1, final_number + 1):
    for j in range(i):
        print(i, end=" ")
    print()
