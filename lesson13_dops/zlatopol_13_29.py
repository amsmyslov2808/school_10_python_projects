import random

PASSENGER_СAR = 1
TRUCK_CAR = 2


def car_type_to_str(car_type):
    if car_type == PASSENGER_СAR:
        return "PASSENGER_СAR"
    elif car_type == TRUCK_CAR:
        return "TRUCK_CAR"

    return "NONE"


def create_cars(prices, types, count_cars):
    for _ in range(count_cars):
        current_price = random.randint(10000, 100000)
        current_type = random.randint(PASSENGER_СAR, TRUCK_CAR)

        prices.append(current_price)
        types.append(current_type)


def get_avg_price_passenger_cars(prices, types, count_cars):
    count_passenger_cars = 0
    sum_price_passenger_cars = 0

    for i in range(count_cars):
        if types[i] == PASSENGER_СAR:
            count_passenger_cars += 1
            sum_price_passenger_cars += prices[i]

    return sum_price_passenger_cars / count_passenger_cars


def pritty_print_cars(prices, types, count_cars):
    for i in range(count_cars):
        print(f"#{i+1} type:{car_type_to_str(types[i])} price:${prices[i]}")


prices = []
types = []
count_cars = 3

create_cars(prices, types, count_cars)
pritty_print_cars(prices, types, count_cars)

print(
    f"avg price passenger cars = {get_avg_price_passenger_cars(prices, types, count_cars):.2f}"
)
