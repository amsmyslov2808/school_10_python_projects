import os
from dataclasses import dataclass

ID = 4


@dataclass
class GamePC:
    id: int
    fabricator: str
    cpu: str
    gpu: str
    ram: int
    ssd: int
    weight: int
    price: int
    count: int


PCs = []


def find_ind_PC_by_id(PCs, id):
    for ind in range(len(PCs)):
        if PCs[ind].id == id:
            return ind
    else:
        return -1


def input_correct(text):
    is_correct_input = False
    while is_correct_input == False:
        try:
            result = int(input(text))
            is_correct_input = True
        except:
            print("Ошибка ввода, попробуй ещё раз")
            is_correct_input = False
    return result


def add_PC(PCs, PC):
    global ID

    ID += 1

    PC.id = ID

    PCs.append(PC)
    os.system("cls")


def parameter_input():
    fabricator = input("введите производителя:")
    cpu = input("введите название процессора:")
    gpu = input_correct("введите количество видеопамяти графического процессора:")
    ram = input_correct("введите количество оперативной памяти:")
    ssd = input_correct("введите количество внутренней памяти:")
    weight = input_correct("введите вес компьютера:")
    price = input_correct("введите стоимость компьютера:")
    count = input_correct("введите количество товара на складе:")

    return GamePC(0, fabricator, cpu, gpu, ram, ssd, weight, price, count)


def print_PC(PCs):
    os.system("cls")
    print(
        f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}"
    )

    for i in range(len(PCs)):
        print(
            f"{PCs[i].id:<8}{PCs[i].fabricator:<15}{PCs[i].cpu:<15}"
            f"{PCs[i].gpu:<15}{PCs[i].ram:<15}{PCs[i].ssd:<15}"
            f"{PCs[i].weight:<7}{PCs[i].price:<10}{PCs[i].count:<15}"
        )


def print_best_bat(PCs):
    best = PCs[0].price
    bad = PCs[0].price
    ind_best = 0
    ind_bad = 0
    for best_price in range(len(PCs)):
        if PCs[best_price].price > best:
            best = PCs[best_price].price
            ind_best = best_price
    for bad_price in range(len(PCs)):
        if PCs[bad_price].price < bad:
            bad = PCs[bad_price].price
            ind_bad = bad_price

    os.system("cls")

    print(
        f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}"
    )
    print("Самый дорогой:")
    print(
        f"{PCs[ind_best].id:<8}{PCs[ind_best].fabricator:<15}{PCs[ind_best].cpu:<15}"
        f"{PCs[ind_best].gpu:<15}{PCs[ind_best].ram:<15}{PCs[ind_best].ssd:<15}"
        f"{PCs[ind_best].weight:<7}{PCs[ind_best].price:<10}{PCs[ind_best].count:<15}"
    )
    print("Самый дешёвый:")
    print(
        f"{PCs[ind_bad].id:<8}{PCs[ind_bad].fabricator:<15}{PCs[ind_bad].cpu:<15}"
        f"{PCs[ind_bad].gpu:<15}{PCs[ind_bad].ram:<15}{PCs[ind_bad].ssd:<15}"
        f"{PCs[ind_bad].weight:<7}{PCs[ind_bad].price:<10}{PCs[ind_bad].count:<15}"
    )


def up_RAM(PCs, id, up):
    os.system("cls")
    ind = find_ind_PC_by_id(PCs, id)
    if ind != -1:
        PCs[ind].ram += up
        print(f"Изменение памяти компьютера с id {id} успешно завершено")
    else:
        print(f"компьютера с id {id} не существует")


def sale(PCs, id):
    os.system("cls")
    ind = find_ind_PC_by_id(PCs, id)
    if ind != -1:
        PCs[ind].price -= PCs[ind].price * 0.1
        print(f"Компьютер с id {id} выстовлен на распрадажу")
    else:
        print(f"компьютера с id {id} не существует")


def del_PC_id(PCs, id):
    os.system("cls")
    ind = find_ind_PC_by_id(PCs, id)
    if ind != -1:
        PCs.pop(ind)
        print(f"Компьютер с id {id} успешно удален")
    else:
        print(f"компьютера с id {id} не существует")


def del_PC_ind(PCs, ind):
    os.system("cls")
    try:
        PCs.pop(ind)
    except:
        print(f"Компьютера с индексом {ind} не существует")


def print_ind_PC(PCs, ind):
    os.system("cls")
    try:
        print(
            f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}"
        )
        print(
            f"{PCs[ind].id:<8}{PCs[ind].fabricator:<15}{PCs[ind].cpu:<15}"
            f"{PCs[ind].gpu:<15}{PCs[ind].ram:<15}{PCs[ind].ssd:<15}"
            f"{PCs[ind].weight:<7}{PCs[ind].price:<10}{PCs[ind].count:<15}"
        )
    except:
        print(f"Компьютера с индексом {ind} не существует")


def compare_GPU(PCs, min_har):
    print_only_heading()
    for ind in range(len(PCs)):
        if PCs[ind].gpu > min_har:
            print_ind_PC(PCs, ind)


def print_only_heading():
    print(
        f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}"
    )


def print_1_pc(PC):
    print(
        f"{PC.id:<8}{PC.fabricator:<15}{PC.cpu:<15}"
        f"{PC.gpu:<15}{PC.ram:<15}{PC.ssd:<15}"
        f"{PC.weight:<7}{PC.price:<10}{PC.count:<15}"
    )


def sorted_PC_price(PCs):
    sort = True
    mid_glass = 0
    while sort:
        sort = False
        for i in range(len(PCs) - 1):
            if PCs[i].price < PCs[i + 1].price:
                mid_glass = PCs[i + 1]
                PCs[i + 1] = PCs[i]
                PCs[i] = mid_glass
                sort = True
    print_PC(PCs)


def searc_PC(PCs, min_ram, max_price):
    os.system("cls")
    print("\nПОИСК ПО ОЗУ И ЦЕНЕ")

    results = []
    for pc in PCs:
        if pc.ram >= min_ram and pc.price <= max_price:
            results.append(pc)

    if results:
        print(
            f"\nНайдено {len(results)} компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}:"
        )
        print_PC(results)
    else:
        print(f"\nНет компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}")


def menu():
    global GAME_RUN
    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) Добавить компьютер")
    print("2) Показать все компьютеры")
    print("3) Поиск компьютеров")
    print("4) Сортировка по цене")
    print("5) Самый дорогой/дешевый")
    print("6) увеличить оперативную память ПК")
    print("7) удалить ПК")
    print("8) поставить на распродажу")
    print("9) поиск GPU по его минимальным характеристикам")
    print("0) Выход")
    result = int(input("сделай выбор:"))

    if result == 1:
        os.system("cls")
        add_PC(PCs, parameter_input())
    elif result == 2:
        os.system("cls")
        print_PC(PCs)
    elif result == 3:
        os.system("cls")
        min_ram = input_correct(
            "введите минимальное количество оперативной памяти в пк (ГБ):"
        )
        max_price = input_correct("введите максимальную стоимость компьютера:")
        searc_PC(PCs, min_ram, max_price)
    elif result == 4:
        os.system("cls")
        sorted_PC_price(PCs)
    elif result == 5:
        os.system("cls")
        print_best_bat(PCs)
    elif result == 6:
        os.system("cls")
        id = input_correct("введите ID ПК:")
        up_ram = input_correct(
            "введите количество оперативной памяти которую вы хотите добавить:"
        )
        up_RAM(PCs, id, up_ram)
    elif result == 7:
        os.system("cls")
        result_7 = input_correct(
            "как вы хотите удалить пк (1 - по ID, 2 - по индексу):"
        )
        if result_7 == 1:
            id_PC = 0
            os.system("cls")
            id_PC = input_correct("введите ID ПК:")
            del_PC_id(PCs, id_PC)
        else:
            os.system("cls")
            ind_PC = input_correct("введите INDEX ПК:")
            del_PC_ind(PCs, ind_PC)
    elif result == 8:
        os.system("cls")
        sale_id = input_correct("введте ID ПК которому вы хотите сделать скидку:")
        sale(PCs, sale_id)
    elif result == 9:
        os.system("cls")
        har = input_correct(
            "введите минимальную характеристику видеокарте (ГБ видеопамяти):"
        )
        compare_GPU(PCs, har)
    else:
        os.system("cls")
        GAME_RUN = False
        return GAME_RUN


PCs.append(GamePC(1, 1, 1, 16, 1, 1, 1, 180000, 1))
PCs.append(GamePC(2, 2, 2, 32, 2, 2, 2, 120000, 2))
PCs.append(GamePC(3, 1, 1, 16, 1, 1, 1, 200000, 1))
PCs.append(GamePC(4, 2, 2, 32, 2, 2, 2, 300000, 2))
GAME_RUN = True
while GAME_RUN:
    menu()
