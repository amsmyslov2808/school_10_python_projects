from dataclasses import dataclass


@dataclass
class Student:
    age: int
    name: str
    lastname: str


students = []
students.append(Student(15, "Катя", "Чекрыгина"))
students.append(Student(13, "Ульяна", "Шевердина"))
students.append(Student(12, "Макар", "А"))

min_age_student_index = 0

for i in range(len(students)):
    if students[i].age < students[min_age_student_index].age:
        min_age_student_index = i

print(f"минимальный возраст студента = {students[min_age_student_index].age}")
print(students[min_age_student_index])
print(f"индекс студента = {min_age_student_index}")

# min_age = students[0].age
# min_age_student = students[0]
# min_age_student_index = 0

# for index, item in enumerate(students):
#     if item.age < min_age:
#         min_age = item.age
#         min_age_student = item
#         min_age_student_index = index

# print(f"минимальный возраст студента = {min_age}")
# print(min_age_student)
# print(f"индекс студента = {min_age_student_index}")
