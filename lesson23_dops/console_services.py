import os


def clear_console() -> None:
    # 'nt' означает Windows, 'posix' — Linux или macOS
    os.system("cls" if os.name == "nt" else "clear")


def input_int(message: str, min_number: int, max_number: int) -> int:
    is_correct_input = False
    number = 0

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


def input_str(message: str, min_length: int, max_length: int) -> str:
    is_correct_input = False
    str_data = ""

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


def check_enter() -> None:
    input()


def print_devider() -> None:
    print("=" * 15)
    print()
