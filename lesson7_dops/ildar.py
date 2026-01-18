sec_from_midnight = int(input("введите кол-во секунд с начала суток: "))

secs = sec_from_midnight % 60
temp_min = sec_from_midnight // 60
hours = temp_min // 60
mins = temp_min % 60

print(f"{sec_from_midnight} = {hours}:{mins}:{secs}")
