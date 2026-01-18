for i in range(1, 10 + 1):
    if i == 5:
        continue
    for j in range(1, 10 + 1):
        if j == 8:
            break
        print(i * j, end=" ")

    print()
