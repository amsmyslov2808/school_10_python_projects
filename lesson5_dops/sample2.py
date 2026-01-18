count_students = 0
current_jump_dist = 0
sum_dist = 0
avg_dist = 0

while current_jump_dist != -1:
    current_jump_dist = int(input("введите дистанцию прыжка очередного студента: "))

    if current_jump_dist != -1:
        sum_dist = sum_dist + current_jump_dist
        count_students = count_students + 1

avg_dist = sum_dist / count_students


print(f"средняя дистанция прыжка = {avg_dist:.2f}")
