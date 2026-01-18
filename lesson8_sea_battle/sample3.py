import random

is_stop = False

while not is_stop:
    print("hello")

    if random.randint(1, 1000 + 1) < 500:
        is_stop = True
