numbers = input()
numbers_list = numbers.split()

a = int(numbers_list[0])
b = int(numbers_list[1])
c = int(numbers_list[2])

if a < 94 or a > 727 or b < 94 or b > 727 or c < 94 or c > 727:
    print("Error")
else:
    max_num = 0
    if a > b:
        max_num = a
    else:
        max_num = b

    if c > max_num:
        max_num = c

    print(max_num)


# numbers = input()
# numbers_list = numbers.split()
# numbers_int_list = []

# for item in numbers_list:
#     numbers_int_list.append(int(item))

# has_error = False

# for item in numbers_int_list:
#     if item < 94 or item > 727:
#         has_error = True
#         break

# if has_error == True:
#     print("Error")
# else:
#     print(max(numbers_int_list))

mass = input().split()
a = int(mass[0])
b = int(mass[1])
c = int(mass[2])
if a < 94 or a > 727:
    print("Error")
else:
    if b < 94 or b > 727:
        print("Error")
    else:
        if c < 94 or c > 727:
            print("Error")
        else:

            if a >= b:
                if a >= c:
                    print(a)
                else:
                    if b >= c:
                        print(b)
                    else:
                        if c >= b:
                            print(c)
