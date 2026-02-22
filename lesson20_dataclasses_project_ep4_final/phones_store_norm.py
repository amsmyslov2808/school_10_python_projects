import os
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
#     Состояние - число (от 1 до 5)
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

BRAND_MIN_LEN = 1
BRAND_MAX_LEN = 10

MODEL_MIN_LEN = 1
MODEL_MAX_LEN = 15

WEIGHT_MIN = 100
WEIGHT_MAX = 2000

SCREEN_MIN = 2.0
SCREEN_MAX = 10.0

BATTERY_MIN = 1500
BATTERY_MAX = 20000

STATUS_MIN = 1
STATUS_MAX = 5

PRICE_MIN = 1500
PRICE_MAX = 200000

AMOUNT_MIN = 1
AMOUNT_MAX = 1000

FILE_NAME_MIN_LEN = 5
FILE_NAME_MAX_LEN = 40


# действия пользователя в программе
def clear_console() -> None:
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


# 1) искать Мобильные телефоны по:
#     Марка
def get_phones_by_brand(phones: list[MobilePhone], brand: str) -> list[MobilePhone]:
    return [item for item in phones if item.brand.lower() == brand.lower()]


#     Цена
def get_phones_by_price(phones: list[MobilePhone], price: int) -> list[MobilePhone]:
    return [item for item in phones if item.price == price]


#     Состояние
def get_phones_by_status(phones: list[MobilePhone], status: int) -> list[MobilePhone]:
    return [item for item in phones if item.status == status]


# 11) найти все телефоны с минимальной ценой:
def get_phones_with_min_price(phones: list[MobilePhone]) -> list[MobilePhone]:
    if len(phones) == 0:
        return []

    min_price = min(item.price for item in phones)

    return [item for item in phones if item.price == min_price]


# 2) сортировать Мобильные телефоны по:
#     ИД


def sort_phones_by_id(phones: list[MobilePhone], order: str) -> None:
    phones.sort(key=lambda item: item.id, reverse=(order == DESC))

    print("список телефонов по ИД успешно отсортирован")


#     Цена
def sort_phones_by_price(phones: list[MobilePhone], order: str) -> None:
    phones.sort(key=lambda item: item.price, reverse=(order == DESC))

    print("список телефонов по Цене успешно отсортирован")


#     Диагональ экрана
def sort_phones_by_screen_diagonal(phones: list[MobilePhone], order: str) -> None:
    phones.sort(key=lambda item: item.screen_diagonal, reverse=(order == DESC))

    print("список телефонов по Диагонали экрана успешно отсортирован")


#     Ёмкость аккумултора
def sort_phones_by_battery(phones: list[MobilePhone], order: str) -> None:
    phones.sort(key=lambda item: item.battery, reverse=(order == DESC))

    print("список телефонов по ёмкости аккумулятора успешно отсортирован")


#     Вес
def sort_phones_by_weight(phones: list[MobilePhone], order: str) -> None:
    phones.sort(key=lambda item: item.weight, reverse=(order == DESC))

    print("список телефонов по весу успешно отсортирован")


# 3) добавлять новые мобильные телефоны в список телефонов


def input_int(message: str, min_number: int, max_number: int) -> int:
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
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_float(message: str, min_number: float, max_number: float) -> float:
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
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_str(message: str, min_length: int, max_length: int) -> str:
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


def input_phone_data() -> MobilePhone:
    print("Введите данные телефона")

    brand = input_str("марку: ", BRAND_MIN_LEN, BRAND_MAX_LEN)
    model = input_str("модель: ", MODEL_MIN_LEN, MODEL_MAX_LEN)
    weight = input_int("вес: ", WEIGHT_MIN, WEIGHT_MAX)
    screen_diagonal = input_float("диагональ экрана: ", SCREEN_MIN, SCREEN_MAX)
    battery = input_int("ёмкость акумулятора: ", BATTERY_MIN, BATTERY_MAX)
    status = input_int("статус (от 1 до 5): ", STATUS_MIN, STATUS_MAX)
    price = input_int("цену: ", PRICE_MIN, PRICE_MAX)
    amount = input_int("количество на складе: ", AMOUNT_MIN, AMOUNT_MAX)

    return MobilePhone(
        0, brand, model, weight, screen_diagonal, battery, status, price, amount
    )


def add_phone_to_list(phones: list[MobilePhone], phone: MobilePhone) -> None:
    global GLOBAL_MOBILE_PHONE_ID
    GLOBAL_MOBILE_PHONE_ID += 1

    phone.id = GLOBAL_MOBILE_PHONE_ID

    phones.append(phone)

    print("Телефон успешно добавлен в список телефонов")


# 4) удалять мобильные телефоны из списка телефонов по ИД
def find_phone_index_by_id(phones: list[MobilePhone], id: int) -> int:
    # finded = [index for index, item in enumerate(phones) if item.id == id]

    # if len(finded) == 0:
    #     return -1

    # return finded[0]

    for i in range(len(phones)):
        if phones[i].id == id:
            return i

    return -1


def delete_phone_by_id(phones: list[MobilePhone], id: int) -> None:
    delete_index = find_phone_index_by_id(phones, id)

    if delete_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    phones.pop(delete_index)
    print(f"Телефон с id = {id} успешно удалён")


# 5) изменить поле "Количество на складе" в сущности мобильный телефон по ИД
def change_phone_amount(phones: list[MobilePhone], id: int, new_amount: int) -> None:
    change_index = find_phone_index_by_id(phones, id)

    if change_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    phones[change_index].amount = new_amount

    print(
        f"Количество на складе у телефон с id = {id} успешно изменено на {new_amount}"
    )


# 6) изменить всю информацию о мобильном телефоне, кроме поля ИД, предварительно найдя его по ИД
def change_phone_information(phones: list[MobilePhone], id: int) -> None:
    change_index = find_phone_index_by_id(phones, id)

    if change_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    new_phone_data = input_phone_data()

    phones[change_index].brand = new_phone_data.brand
    phones[change_index].model = new_phone_data.model
    phones[change_index].weight = new_phone_data.weight
    phones[change_index].screen_diagonal = new_phone_data.screen_diagonal
    phones[change_index].battery = new_phone_data.battery
    phones[change_index].status = new_phone_data.status
    phones[change_index].price = new_phone_data.price
    phones[change_index].amount = new_phone_data.amount

    print(f"Параметры у телефон с id = {id} успешно изменены")


# 7) вывести список всех мобильных телефонов
def print_phones(phones: list[MobilePhone]) -> None:
    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес(гр)':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )

    if len(phones) == 0:
        print("Список пуст")
        return

    for item in phones:
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{str(item.status)+'/5':<15}{item.price:<15}{item.amount:<15}"
        )


# 8) вывести мобильный телефон по ИД
def print_phone_by_id(phones: list[MobilePhone], id: int) -> None:
    print_index = find_phone_index_by_id(phones, id)

    if print_index == -1:
        print(f"Телефон с id = {id} не найден")
        return

    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )
    item = phones[print_index]
    print(
        f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{str(item.status)+'/5':<15}{item.price:<15}{item.amount:<15}"
    )


# 9) сохранить список мобильных телефонов в текстовый файл, в двух вариантах
#     для удобного чтения человеком
#     для последующей удобной загрузки компьютером в эту программу (по одному полю на строку)


def save_to_txt_for_human(phones: list[MobilePhone], filename: str) -> None:
    try:
        file_out = open(filename, "w", encoding="utf-8")
        file_out.write(
            f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес(гр)':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}\n"
        )

        for item in phones:
            file_out.write(
                f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{str(item.status)+'/5':<15}{item.price:<15}{item.amount:<15}\n"
            )
        file_out.close()

        print(f"Телефоны в человекочитаемов виде в файл {filename} успешно сохранены")
    except:
        print(f"Ошибка при сохранениии телефонов в файл {filename}")


def save_to_txt_for_computer(phones: list[MobilePhone], filename: str) -> None:
    try:
        file_out = open(filename, "w", encoding="utf-8")
        global GLOBAL_MOBILE_PHONE_ID
        file_out.write(f"{GLOBAL_MOBILE_PHONE_ID}\n")
        file_out.write(f"{len(phones)}\n")

        for item in phones:
            file_out.write(
                f"{item.id}\n{item.brand}\n{item.model}\n{item.weight}\n{item.screen_diagonal}\n{item.battery}\n{item.status}\n{item.price}\n{item.amount}\n"
            )
        file_out.close()

        print(f"Телефоны в машиночитаемом виде в файл {filename} успешно сохранены")
    except:
        print(f"Ошибка при сохранениии телефонов в файл {filename}")


# 10) загрузить список мобильных телефонов из текстового файла


def load_from_txt_for_computer(filename: str) -> list[MobilePhone]:
    phones: list[MobilePhone] = []

    try:
        file_in = open(filename, "r", encoding="utf-8")
        global GLOBAL_MOBILE_PHONE_ID
        GLOBAL_MOBILE_PHONE_ID = int(file_in.readline())
        count_phones = int(file_in.readline())

        for _ in range(count_phones):
            id = int(file_in.readline())
            brand = file_in.readline().strip()
            model = file_in.readline().strip()
            weight = int(file_in.readline())
            screen_diagonal = float(file_in.readline())
            battery = int(file_in.readline())
            status = int(file_in.readline())
            price = int(file_in.readline())
            amount = int(file_in.readline())

            phones.append(
                MobilePhone(
                    id,
                    brand,
                    model,
                    weight,
                    screen_diagonal,
                    battery,
                    status,
                    price,
                    amount,
                )
            )

        file_in.close()

        print(f"Телефоны из файла {filename} успешно загружены")
    except:
        print(f"Ошибка при загрузке телефонов из файла {filename}")

    return phones


def process_add_phone_menu(phones: list[MobilePhone]) -> None:
    add_phone_to_list(phones, input_phone_data())


def process_delete_phone_menu(phones: list[MobilePhone]) -> None:
    id = input_int("Введите ИД телефона для удаления: ", 1, GLOBAL_MOBILE_PHONE_ID)
    delete_phone_by_id(phones, id)


def process_save_human_menu(phones: list[MobilePhone]) -> None:
    filename = input_str(
        "Введите имя файла для сохранения: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    save_to_txt_for_human(phones, filename)


def process_save_computer_menu(phones: list[MobilePhone]) -> None:
    filename = input_str(
        "Введите имя файла для сохранения: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    save_to_txt_for_computer(phones, filename)


def process_load_computer_menu() -> list[MobilePhone]:
    filename = input_str(
        "Введите имя файла для загрузки: ", FILE_NAME_MIN_LEN, FILE_NAME_MAX_LEN
    )
    return load_from_txt_for_computer(filename)


def process_change_information_menu(phones: list[MobilePhone]) -> None:
    id = input_int("Введите ИД телефона для обновления: ", 1, GLOBAL_MOBILE_PHONE_ID)
    change_phone_information(phones, id)


def process_change_amount_menu(phones: list[MobilePhone]) -> None:
    id = input_int("Введите ИД телефона для обновления: ", 1, GLOBAL_MOBILE_PHONE_ID)
    amount = input_int(
        "Введите новое количество телефонов на складе: ", AMOUNT_MIN, AMOUNT_MAX
    )
    change_phone_amount(phones, id, amount)


def process_print_phone_by_id_menu(phones: list[MobilePhone]) -> None:
    id = input_int("Введите ИД телефона для вывода: ", 1, GLOBAL_MOBILE_PHONE_ID)
    print_phone_by_id(phones, id)


def process_exit_menu() -> bool:
    print("Для завершения работы программы нажмите <Enter>")
    return False


def process_sort_menu(phones: list[MobilePhone]) -> None:
    print("Выберите первый параметр сортировки")

    print("1. ИД")
    print("2. Цена")
    print("3. Диагональ экрана")
    print("4. Ёмкость аккумулятора")
    print("5. Вес телефона")

    sort_point = input_int("Выберите пункт меню: ", 1, 5)

    print("Выберите второй параметр сортировки")

    print("1. По возрастанию")
    print("2. По убыванию")

    order_point = input_int("Выберите пункт меню: ", 1, 2)

    order = ""
    if order_point == 1:
        order = ASC
    elif order_point == 2:
        order = DESC

    if sort_point == 1:
        sort_phones_by_id(phones, order)
    elif sort_point == 2:
        sort_phones_by_price(phones, order)
    elif sort_point == 3:
        sort_phones_by_screen_diagonal(phones, order)
    elif sort_point == 4:
        sort_phones_by_battery(phones, order)
    elif sort_point == 5:
        sort_phones_by_weight(phones, order)


def process_find_menu(phones: list[MobilePhone]) -> None:
    print("Выберите первый параметр поиска")

    print("1. Марка")
    print("2. Цена")
    print("3. Статус")

    find_point = input_int("Выберите пункт меню: ", 1, 3)

    finded_phones: list[MobilePhone] = []

    if find_point == 1:
        brand = input_str("Введите название марки: ", BRAND_MIN_LEN, BRAND_MAX_LEN)
        finded_phones = get_phones_by_brand(phones, brand)
    elif find_point == 2:
        price = input_int("Введите цену телефона: ", PRICE_MIN, PRICE_MAX)
        finded_phones = get_phones_by_price(phones, price)
    elif find_point == 3:
        status = input_int(
            "Введите статус телефона (от 1 до 5): ", STATUS_MIN, STATUS_MAX
        )
        finded_phones = get_phones_by_status(phones, status)

    print_phones(finded_phones)


def print_main_menu() -> None:
    print("\n============\n")

    print("======МЕНЮ======")
    print("1. Добавить новый телефон в список")
    print("2. Удалить телефон из списка по ИД")
    print("3. Сохранить список телефонов в человекочитаемый файл")
    print("4. Сохранить список телефонов в машиночитаемый файл")
    print("5. Загрузить список телефонов из машиночитаемого файла")
    print("6. Обновить информацию о телефоне по ИД")
    print("7. Обновить количество на складе по ИД")
    print("8. Отсортировать список телефонов по ...")
    print("9. Найти мобильные телефоны по ...")
    print("10. Вывести телефон по ИД")
    print("11. Вывести все телефоны с минимальной ценой")
    print("0. Выйти из программы")


phones: list[MobilePhone] = []

is_run = True
while is_run == True:
    clear_console()

    print_phones(phones)

    print_main_menu()

    menu_point = input_int("Выберите пункт меню: ", 0, 11)

    if menu_point == 1:
        process_add_phone_menu(phones)
    elif menu_point == 2:
        process_delete_phone_menu(phones)
    elif menu_point == 3:
        process_save_human_menu(phones)
    elif menu_point == 4:
        process_save_computer_menu(phones)
    elif menu_point == 5:
        phones = process_load_computer_menu()
    elif menu_point == 6:
        process_change_information_menu(phones)
    elif menu_point == 7:
        process_change_amount_menu(phones)
    elif menu_point == 8:
        process_sort_menu(phones)
    elif menu_point == 9:
        process_find_menu(phones)
    elif menu_point == 10:
        process_print_phone_by_id_menu(phones)
    elif menu_point == 11:
        finded_phones = get_phones_with_min_price(phones)
        print_phones(finded_phones)
    elif menu_point == 0:
        is_run = process_exit_menu()
    input()
