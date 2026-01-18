count_students = int(input("введите кол-во студентов, которые пришли на пересдачу: "))

current_mark = 0
sum_marks = 0
avg_mark = 0

for _ in range(count_students):
    current_mark = int(input("введите оценку очередного студента: "))
    sum_marks = sum_marks + current_mark

avg_mark = sum_marks / count_students


print(f"средняя оценка = {avg_mark:.2f}")
