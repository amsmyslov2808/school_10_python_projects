from dataclasses import dataclass

# сущность:
#     МобильныйТелефон
# поля:
#     ИД - целое уникальное число
#     Марка - строка (от 1 до 10 символов)
#     Модель - строка (от 1 до 15 символов)
#     Вес - целое число (от 100 до 2000)
#     Диагональ экрана - дробное число (от 2 до 10)
#     Ёмкость аккумултора - целое число (от 1500 до 20000)
#     Состояние - строка (от 5 до 10 символов)
#     Цена - целое число (от 1500 до 200000)
#     Количество на складе - целое число (от 1 до 1000)


@dataclass
class MobilePhone:
    id: int
    brand: str
    model: str
    weight: int
    screen_diagonal: float
    battery: int
    status: int
    price: int
    amount: int


GLOBAL_MOBILE_PHONE_ID = 0

ASC = "ascending"
DESC = "descending"

# действия пользователя в программе


# 1) искать Мобильные телефоны по:
#     Марка
def get_phones_by_brand(phones, brand):
    finded_phones = []

    for item in phones:
        if item.brand == brand:
            finded_phones.append(item)

    return finded_phones


#     Цена
def get_phones_by_price(phones, price):
    finded_phones = []

    for item in phones:
        if item.price == price:
            finded_phones.append(item)

    return finded_phones


#     Состояние
def get_phones_by_status(phones, status):
    finded_phones = []

    for item in phones:
        if item.status == status:
            finded_phones.append(item)

    return finded_phones


# 2) сортировать Мобильные телефоны по:
#     ИД
def is_swap(number_current, number_next, order):
    if order == ASC:
        if number_next < number_current:
            return True
        else:
            return False
    elif order == DESC:
        if number_next > number_current:
            return True
        else:
            return False


def sort_phones_by_id(phones, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(phones) - 1 - offset):
            if is_swap(phones[i].id, phones[i + 1].id, order):
                temp = phones[i + 1]
                phones[i + 1] = phones[i]
                phones[i] = temp
                is_sorted = False

        offset += 1


#     Цена
def sort_phones_by_price(phones, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(phones) - 1 - offset):
            if is_swap(phones[i].price, phones[i + 1].price, order):
                temp = phones[i + 1]
                phones[i + 1] = phones[i]
                phones[i] = temp
                is_sorted = False

        offset += 1


#     Диагональ экрана
def sort_phones_by_screen_diagonal(phones, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(phones) - 1 - offset):
            if is_swap(phones[i].screen_diagonal, phones[i + 1].screen_diagonal, order):
                temp = phones[i + 1]
                phones[i + 1] = phones[i]
                phones[i] = temp
                is_sorted = False

        offset += 1


#     Ёмкость аккумултора
def sort_phones_by_battery(phones, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(phones) - 1 - offset):
            if is_swap(phones[i].battery, phones[i + 1].battery, order):
                temp = phones[i + 1]
                phones[i + 1] = phones[i]
                phones[i] = temp
                is_sorted = False

        offset += 1


#     Вес
def sort_phones_by_weight(phones, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(phones) - 1 - offset):
            if is_swap(phones[i].weight, phones[i + 1].weight, order):
                temp = phones[i + 1]
                phones[i + 1] = phones[i]
                phones[i] = temp
                is_sorted = False

        offset += 1


# 3) добавлять новые мобильные телефоны в список телефонов


def input_int(message, min_number, max_number):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = int(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_float(message, min_number, max_number):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = float(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_str(message, min_length, max_length):
    is_correct_input = False

    while is_correct_input == False:
        str_data = input(message).strip()

        if len(str_data) < min_length or len(str_data) > max_length:
            print(
                f"Ошибка ввода. Количество символов должно быть в границах от {min_length} до {max_length}"
            )
            is_correct_input = False
        else:
            is_correct_input = True

    return str_data


def input_phone_data():
    print("введите данные телефона")

    brand = input_str("марку: ", 1, 10)
    model = input_str("модель: ", 1, 15)
    weight = input_int("вес: ", 100, 2000)
    screen_diagonal = input_float("диагональ экрана: ", 2, 10)
    battery = input_int("ёмкость акумулятора: ", 1500, 20000)
    status = input_int("статус (от 1 до 5): ", 1, 5)
    price = input_int("цену: ", 1500, 200000)
    amount = input_int("количество на складе: ", 1, 1000)

    return MobilePhone(
        0, brand, model, weight, screen_diagonal, battery, status, price, amount
    )


def add_phone_to_list(phones, phone):
    global GLOBAL_MOBILE_PHONE_ID
    GLOBAL_MOBILE_PHONE_ID += 1

    phone.id = GLOBAL_MOBILE_PHONE_ID

    phones.append(phone)


# 4) удалять мобильные телефоны из списка телефонов по ИД
def find_phone_index_by_id(phones, id):
    for i in range(len(phones)):
        if phones[i].id == id:
            return i

    return -1


def delete_phone_by_id(phones, id):
    delete_index = find_phone_index_by_id(phones, id)

    if delete_index != -1:
        phones.pop(delete_index)
        print(f"Телефон с id = {id} успешно удалён")


# 5) изменить поле "Количество на складе" в сущности мобильный телефон по ИД
def change_phone_amount(phones, id, new_amount):
    change_index = find_phone_index_by_id(phones, id)

    if change_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    if new_amount < 1 or new_amount > 1000:
        print(
            f"Новое количество на складе неверно. Оно должно быть в диапазоне от 1 до 1000"
        )
        return

    phones[change_index].amount = new_amount

    print(
        f"Количество на складе у телефон с id = {id} успешно изменено на {new_amount}"
    )


# 6) изменить всю информацию о мобильном телефоне, кроме поля ИД, предварительно найдя его по ИД
def change_phone_information(phones, id):
    change_index = find_phone_index_by_id(phones, id)

    if change_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    new_phone_data = input_phone_data()

    phones[change_index].brand = new_phone_data.brand
    phones[change_index].model = new_phone_data.brand
    phones[change_index].weight = new_phone_data.weight
    phones[change_index].screen_diagonal = new_phone_data.screen_diagonal
    phones[change_index].battery = new_phone_data.battery
    phones[change_index].status = new_phone_data.status
    phones[change_index].price = new_phone_data.price
    phones[change_index].amount = new_phone_data.amount

    print(f"Параметры у телефон с id = {id} успешно изменены")


# 7) вывести список всех мобильных телефонов
def print_phones(phones):
    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес(гр)':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )

    for item in phones:
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{str(item.status)+'/5':<15}{item.price:<15}{item.amount:<15}"
        )


# 8) вывести мобильный телефон по ИД
def print_phone_by_id(phones, id):
    print_index = find_phone_index_by_id(phones, id)

    if print_index != -1:
        print(
            f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
        )
        item = phones[print_index]
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{str(item.status)+'/5':<15}{item.price:<15}{item.amount:<15}"
        )
    else:
        print(f"Телефон с id = {id} не найден")


# 9) сохранить список мобильных телефонов в текстовый файл, в двух вариантах
#     для удобного чтения человеком
#     для последующей удобной загрузки компьютером в эту программу (по одному полю на строку)

# 10) загрузить список мобильных телефонов из текстового файла

phones = []

# add_phone_to_list(phones, input_phone_data())
# add_phone_to_list(phones, input_phone_data())

# add_phone_to_list(phones, MobilePhone(1, "brand1", "model1", 10, 3.4, 228, 2, 123, 10))
# add_phone_to_list(phones, MobilePhone(2, "brand2", "model2", 10, 3, 228, 3, 123, 10))

# print_phones(phones)

# delete_phone_by_id(phones, 3)

# print_phones(phones)

# print_phone_by_id(phones, 1)
