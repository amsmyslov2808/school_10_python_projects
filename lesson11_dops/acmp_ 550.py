year = int(input())

normalized_year = ""

if year >= 1000:
    normalized_year = str(year)
elif year >= 100 and year <= 999:
    normalized_year = "0" + str(year)
elif year >= 10 and year <= 99:
    normalized_year = "00" + str(year)
elif year >= 0 and year <= 9:
    normalized_year = "000" + str(year)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"12/09/{normalized_year}")
else:
    print(f"13/09/{normalized_year}")
