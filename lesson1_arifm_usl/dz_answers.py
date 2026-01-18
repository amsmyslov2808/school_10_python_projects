# 4.36

# t = int(input("введите число минут с начала часа: "))

# sec = t % 5

# if sec == 0:
#     sec = 5

# if sec <= 3:
#     print("зелёный")
# else:
#     print("красный")

a = int(input("введите a: "))
b = int(input("введите b: "))
c = int(input("введите c: "))

minNum = 0
maxNum = 0
middleNum = 0

if a > b:
    maxNum = a
else:
    maxNum = b

if c > maxNum:
    maxNum = c


if a < b:
    minNum = a
else:
    minNum = b

if c < minNum:
    minNum = c


if a > minNum and a < maxNum:
    middleNum = a
elif b > minNum and b < maxNum:
    middleNum = b
elif c > minNum and c < maxNum:
    middleNum = c
else:
    middleNum = -999

print(f"min = {minNum}")
print(f"max = {maxNum}")
print(f"middle = {middleNum}")
