numbers = input()
numbers_list = numbers.split()
a = int(numbers_list[0])
b = int(numbers_list[1])
c = int(numbers_list[2])

if a * b == c:
    print("YES")
else:
    print("NO")
