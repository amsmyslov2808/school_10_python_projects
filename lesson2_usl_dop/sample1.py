year = int(input("введите year: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("visok")
else:
    print("NE visok")


result = 45

if result > 10 and result < 50:
    print()
elif result >= 50 and result < 100:
    print()
else:
    print()
