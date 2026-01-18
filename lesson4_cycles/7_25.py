count_students = 3
current_mark = 0
count_fives = 0

for i in range(1, count_students + 1):
    current_mark = int(input(f"введите оценку {i} ученика: "))

    if current_mark == 5:
        # count_fives = count_fives + 1
        count_fives += 1

print(f"кол-во 5-к = {count_fives}")
