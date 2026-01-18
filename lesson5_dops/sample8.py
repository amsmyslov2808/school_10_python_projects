for b in range(0, 10 + 1):
    for k in range(0, 20 + 1):
        for t in range(0, 100 + 1):
            if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
                print(f"b={b} k={k} t={t}")
