a = 100
b = 500
c = 1000

min_zp = 0
max_zp = 0

if a < b:
    min_zp = a
else:
    min_zp = b

if c < min_zp:
    min_zp = c

if a > b:
    max_zp = a
else:
    max_zp = b

if c > min_zp:
    max_zp = c

print(max_zp - min_zp)
