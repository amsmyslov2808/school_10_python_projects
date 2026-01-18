distance = 10

sum_dist = distance

for current_day in range(2, 10 + 1):
    distance = distance + distance * 0.1
    print(f"день №{current_day} дистанция = {distance:.1f} км")

    if current_day <= 7:
        sum_dist = sum_dist + distance

print(f"за 7 дней суммарная дистанция = {sum_dist:.1f} км")
