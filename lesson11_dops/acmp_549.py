count_guests = int(input())

if count_guests == 1:
    print(0)
else:
    if count_guests % 2 == 0:
        print(count_guests // 2)
    else:
        print(count_guests)
