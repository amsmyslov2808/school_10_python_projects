from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MobilePhone:
    phone_id: int
    brand: str
    model: str
    weight: int
    screen_size: float
    battery_capacity: int
    condition: str
    price: int
    stock_qty: int


MAX_BRAND_LEN = 10
MAX_MODEL_LEN = 15
MAX_CONDITION_LEN = 10


def _input_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")


def _input_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: нужно ввести дробное число.")


def _input_str(prompt: str, max_len: int) -> str:
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Ошибка: строка не должна быть пустой.")
            continue
        if len(raw) > max_len:
            print(f"Ошибка: максимум {max_len} символов.")
            continue
        return raw


def _find_by_id(phones: List[MobilePhone], phone_id: int) -> Optional[MobilePhone]:
    for phone in phones:
        if phone.phone_id == phone_id:
            return phone
    return None


def add_phone(phones: List[MobilePhone]) -> None:
    print("Добавление нового телефона")
    while True:
        phone_id = _input_int("ИД: ")
        if _find_by_id(phones, phone_id) is None:
            break
        print("Ошибка: ИД уже существует.")

    brand = _input_str("Марка: ", MAX_BRAND_LEN)
    model = _input_str("Модель: ", MAX_MODEL_LEN)
    weight = _input_int("Вес: ")
    screen_size = _input_float("Диагональ экрана: ")
    battery_capacity = _input_int("Ёмкость аккумулятора: ")
    condition = _input_str("Состояние: ", MAX_CONDITION_LEN)
    price = _input_int("Цена: ")
    stock_qty = _input_int("Количество на складе: ")

    phones.append(
        MobilePhone(
            phone_id=phone_id,
            brand=brand,
            model=model,
            weight=weight,
            screen_size=screen_size,
            battery_capacity=battery_capacity,
            condition=condition,
            price=price,
            stock_qty=stock_qty,
        )
    )
    print("Телефон добавлен.")


def remove_phone(phones: List[MobilePhone]) -> None:
    phone_id = _input_int("Введите ИД для удаления: ")
    phone = _find_by_id(phones, phone_id)
    if phone is None:
        print("Телефон с таким ИД не найден.")
        return
    phones.remove(phone)
    print("Телефон удалён.")


def update_stock_qty(phones: List[MobilePhone]) -> None:
    phone_id = _input_int("Введите ИД: ")
    phone = _find_by_id(phones, phone_id)
    if phone is None:
        print("Телефон с таким ИД не найден.")
        return
    phone.stock_qty = _input_int("Новое количество на складе: ")
    print("Количество на складе обновлено.")


def update_phone_info(phones: List[MobilePhone]) -> None:
    phone_id = _input_int("Введите ИД: ")
    phone = _find_by_id(phones, phone_id)
    if phone is None:
        print("Телефон с таким ИД не найден.")
        return

    print("Введите новые данные (ИД не меняется).")
    phone.brand = _input_str("Марка: ", MAX_BRAND_LEN)
    phone.model = _input_str("Модель: ", MAX_MODEL_LEN)
    phone.weight = _input_int("Вес: ")
    phone.screen_size = _input_float("Диагональ экрана: ")
    phone.battery_capacity = _input_int("Ёмкость аккумулятора: ")
    phone.condition = _input_str("Состояние: ", MAX_CONDITION_LEN)
    phone.price = _input_int("Цена: ")
    phone.stock_qty = _input_int("Количество на складе: ")
    print("Данные телефона обновлены.")


def print_phone(phone: MobilePhone) -> None:
    print(
        " | ".join(
            [
                f"ИД: {phone.phone_id}",
                f"Марка: {phone.brand}",
                f"Модель: {phone.model}",
                f"Вес: {phone.weight}",
                f"Диагональ: {phone.screen_size}",
                f"Батарея: {phone.battery_capacity}",
                f"Состояние: {phone.condition}",
                f"Цена: {phone.price}",
                f"На складе: {phone.stock_qty}",
            ]
        )
    )


def print_all_phones(phones: List[MobilePhone]) -> None:
    if not phones:
        print("Список телефонов пуст.")
        return
    for phone in phones:
        print_phone(phone)


def print_phone_by_id(phones: List[MobilePhone]) -> None:
    phone_id = _input_int("Введите ИД: ")
    phone = _find_by_id(phones, phone_id)
    if phone is None:
        print("Телефон с таким ИД не найден.")
        return
    print_phone(phone)


def search_phones(phones: List[MobilePhone]) -> None:
    if not phones:
        print("Список телефонов пуст.")
        return

    print("Поиск по: 1) ИД 2) Марка 3) Цена 4) Состояние")
    choice = input("Ваш выбор: ").strip()

    results: List[MobilePhone] = []

    if choice == "1":
        phone_id = _input_int("ИД: ")
        phone = _find_by_id(phones, phone_id)
        if phone is not None:
            results = [phone]
    elif choice == "2":
        brand = _input_str("Марка: ", MAX_BRAND_LEN)
        results = [p for p in phones if p.brand == brand]
    elif choice == "3":
        price = _input_int("Цена: ")
        results = [p for p in phones if p.price == price]
    elif choice == "4":
        condition = _input_str("Состояние: ", MAX_CONDITION_LEN)
        results = [p for p in phones if p.condition == condition]
    else:
        print("Неверный выбор.")
        return

    if not results:
        print("Ничего не найдено.")
        return
    for phone in results:
        print_phone(phone)


def sort_phones(phones: List[MobilePhone]) -> None:
    if not phones:
        print("Список телефонов пуст.")
        return

    print("Сортировать по: 1) ИД 2) Цена 3) Диагональ 4) Ёмкость 5) Вес")
    choice = input("Ваш выбор: ").strip()

    key_map = {
        "1": lambda p: p.phone_id,
        "2": lambda p: p.price,
        "3": lambda p: p.screen_size,
        "4": lambda p: p.battery_capacity,
        "5": lambda p: p.weight,
    }

    key_func = key_map.get(choice)
    if key_func is None:
        print("Неверный выбор.")
        return

    phones.sort(key=key_func)
    print("Список отсортирован.")


def _phones_to_human_text(phones: List[MobilePhone]) -> str:
    if not phones:
        return "Список телефонов пуст.\n"

    lines = [
        "ИД | Марка | Модель | Вес | Диагональ | Ёмкость | Состояние | Цена | Кол-во",
        "-" * 75,
    ]
    for p in phones:
        lines.append(
            f"{p.phone_id} | {p.brand} | {p.model} | {p.weight} | {p.screen_size} | "
            f"{p.battery_capacity} | {p.condition} | {p.price} | {p.stock_qty}"
        )
    return "\n".join(lines) + "\n"


def _phones_to_machine_lines(phones: List[MobilePhone]) -> List[str]:
    lines: List[str] = []
    for p in phones:
        lines.extend(
            [
                str(p.phone_id),
                p.brand,
                p.model,
                str(p.weight),
                str(p.screen_size),
                str(p.battery_capacity),
                p.condition,
                str(p.price),
                str(p.stock_qty),
                "",
            ]
        )
    return lines


def save_phones(phones: List[MobilePhone]) -> None:
    if not phones:
        print("Список телефонов пуст.")
        return

    print("Сохранить как: 1) читаемый текст 2) машинный формат")
    choice = input("Ваш выбор: ").strip()
    file_path = input("Путь к файлу: ").strip()

    if choice == "1":
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(_phones_to_human_text(phones))
        print("Сохранено в читаемом формате.")
    elif choice == "2":
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(_phones_to_machine_lines(phones)))
        print("Сохранено в машинном формате.")
    else:
        print("Неверный выбор.")


def _parse_machine_lines(lines: List[str]) -> List[MobilePhone]:
    cleaned = [line.strip() for line in lines if line.strip() != ""]
    phones: List[MobilePhone] = []

    if len(cleaned) % 9 != 0:
        print("Ошибка: некорректный формат файла.")
        return phones

    for idx in range(0, len(cleaned), 9):
        chunk = cleaned[idx : idx + 9]
        try:
            phone = MobilePhone(
                phone_id=int(chunk[0]),
                brand=chunk[1],
                model=chunk[2],
                weight=int(chunk[3]),
                screen_size=float(chunk[4].replace(",", ".")),
                battery_capacity=int(chunk[5]),
                condition=chunk[6],
                price=int(chunk[7]),
                stock_qty=int(chunk[8]),
            )
        except ValueError:
            print("Ошибка: некорректные данные в файле.")
            return []

        if len(phone.brand) > MAX_BRAND_LEN:
            print("Ошибка: слишком длинная марка в файле.")
            return []
        if len(phone.model) > MAX_MODEL_LEN:
            print("Ошибка: слишком длинная модель в файле.")
            return []
        if len(phone.condition) > MAX_CONDITION_LEN:
            print("Ошибка: слишком длинное состояние в файле.")
            return []

        phones.append(phone)

    return phones


def load_phones(phones: List[MobilePhone]) -> None:
    file_path = input("Путь к файлу: ").strip()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        print("Ошибка: не удалось открыть файл.")
        return

    loaded = _parse_machine_lines(lines)
    if not loaded:
        print("Загрузка не выполнена.")
        return

    seen_ids = {p.phone_id for p in loaded}
    if len(seen_ids) != len(loaded):
        print("Ошибка: в файле есть повторяющиеся ИД.")
        return

    phones.clear()
    phones.extend(loaded)
    print("Список телефонов загружен.")


def _print_menu() -> None:
    print(
        """
Меню:
1) Поиск телефонов
2) Сортировка телефонов
3) Добавить телефон
4) Удалить телефон
5) Изменить количество на складе
6) Изменить все данные (кроме ИД)
7) Показать все телефоны
8) Показать телефон по ИД
9) Сохранить список
10) Загрузить список
0) Выход
"""
    )


def main() -> None:
    phones: List[MobilePhone] = [
        MobilePhone(1, "Samsung", "A54", 202, 6.4, 5000, "new", 34990, 12),
        MobilePhone(2, "Apple", "iPhone13", 174, 6.1, 3240, "new", 59990, 5),
        MobilePhone(3, "Xiaomi", "Redmi12", 198, 6.79, 5000, "used", 14990, 20),
        MobilePhone(4, "Nokia", "G22", 196, 6.5, 5050, "new", 12990, 8),
    ]
    actions = {
        "1": search_phones,
        "2": sort_phones,
        "3": add_phone,
        "4": remove_phone,
        "5": update_stock_qty,
        "6": update_phone_info,
        "7": print_all_phones,
        "8": print_phone_by_id,
        "9": save_phones,
        "10": load_phones,
    }

    while True:
        _print_menu()
        choice = input("Ваш выбор: ").strip()
        if choice == "0":
            print("Выход.")
            break
        action = actions.get(choice)
        if action is None:
            print("Неверный выбор.")
            continue
        action(phones)


if __name__ == "__main__":
    main()
