i = 0
n = 100
sum_dist = 0
dist_from_home = 0

while i < n:
    i = i + 1

    current_step_dist = 1 / i
    sum_dist = sum_dist + current_step_dist

    if i % 2 != 0:
        dist_from_home = dist_from_home + current_step_dist
    else:
        dist_from_home = dist_from_home - current_step_dist

print(f"суммарная дистанция: {sum_dist:.3f} km")
print(f"дистанция от дома: {dist_from_home:.3f} km")
