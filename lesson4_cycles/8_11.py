count_workers = 2
count_months = 3
current_salary = 0
sum_salaries = 0

for number_worker in range(1, count_workers + 1):  # 1..12
    for number_month in range(1, count_months + 1):  # 1..3
        current_salary = int(
            input(
                f"введите зарплату {number_worker} работника за {number_month} месяц: "
            )
        )
        sum_salaries += current_salary

print(f"сумма всех зарплат за все месяцы = {sum_salaries}")
