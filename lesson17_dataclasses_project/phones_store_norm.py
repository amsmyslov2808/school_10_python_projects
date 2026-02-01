from dataclasses import dataclass

# сущность:
#     МобильныйТелефон
# поля:
#     ИД - целое уникальное число
#     Марка - строка (макс 10 символов)
#     Модель - строка (макс 15 символов)
#     Вес - целое число
#     Диагональ экрана - дробное число
#     Ёмкость аккумултора - целое число
#     Состояние - строка (макс 10 символов)
#     Цена - целое число
#     Количество на складе - целое число


@dataclass
class MobilePhone:
    id: int
    brand: str
    model: str
    weight: int
    screen_diagonal: float
    battery: int
    status: str
    price: int
    amount: int


GLOBAL_MOBILE_PHONE_ID = 0

# действия пользователя в программе

# 1) искать Мобильные телефоны по:
#     ИД
#     Марка
#     Цена
#     Состояние

# 2) сортировать Мобильные телефоны по:
#     ИД
#     Цена
#     Диагональ экрана
#     Ёмкость аккумултора
#     Вес


# 3) добавлять новые мобильные телефоны в список телефонов
def input_phone_data():
    print("введите данные телефона")

    brand = input("марку: ")
    model = input("модель: ")
    weight = int(input("вес: "))
    screen_diagonal = float(input("диагональ экрана: "))
    battery = int(input("ёмкость акумулятора: "))
    status = input("статус (подержанный, новый): ")
    price = int(input("цену: "))
    amount = int(input("количество на складе: "))

    return MobilePhone(
        0, brand, model, weight, screen_diagonal, battery, status, price, amount
    )


def add_phone_to_list(phones, phone):
    global GLOBAL_MOBILE_PHONE_ID
    GLOBAL_MOBILE_PHONE_ID += 1

    phone.id = GLOBAL_MOBILE_PHONE_ID

    phones.append(phone)


# 4) удалять мобильные телефоны из списка телефонов

# 5) изменить поле "Количество на складе" в сущности мобильный телефон

# 6) изменить всю информацию о мобильном телефоне, кроме поля ИД, предварительно найдя его по ИД


# 7) вывести список всех мобильных телефонов
def print_phones(phones):
    for item in phones:
        print(item)


# 8) вывести мобильный телефон по ИД

# 9) сохранить список мобильных телефонов в текстовый файл, в двух вариантах
#     для удобного чтения человеком
#     для последующей удобной загрузки компьютером в эту программу (по одному полю на строку)

# 10) загрузить список мобильных телефонов из текстового файла

phones = []

add_phone_to_list(phones, input_phone_data())
add_phone_to_list(phones, input_phone_data())

print_phones(phones)
