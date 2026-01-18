number = int(input("введите число: "))

count_deviders = 0

for i in range(1, number + 1):
    if number % i == 0:
        count_deviders = count_deviders + 1

if count_deviders > 2:
    print("составное")
else:
    print("простое")
