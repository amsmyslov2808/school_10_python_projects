count = int(input())
numbers = input().split()
count_subarray = int(input())

for i in range(count_subarray):
    start, end = map(int, input().split())
    print(*numbers[start - 1 : end])
