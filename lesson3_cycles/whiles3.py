distance = 10
max_distance = 100
current_day = 1

while distance < max_distance:
    distance = distance + distance * 0.1
    current_day = current_day + 1

    print(f"день №{current_day} дистанция = {distance:.1f} км")
