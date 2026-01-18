day_in_year = int(input("введите номер дня в году: "))

month_number = day_in_year // 30 + 1
year_season = ""

if month_number in [1, 2, 12]:
    year_season = "зима"
elif month_number in [3, 4, 5]:
    year_season = "весна"
elif month_number in [6, 7, 8]:
    year_season = "лето"
elif month_number in [9, 10, 11]:
    year_season = "осень"

week_number = day_in_year // 7 + 1

print(f"сезон года = {year_season} номер недели = {week_number}")
