import random

CRISS = "X"
CROSS = "O"
EMPTY_CELL = "."

COLS = 3
ROWS = 3

USER1_STEP = "USER1"
USER2_STEP = "USER2"

USER1_WINNER = "USER1"
USER2_WINNER = "USER2"
NOBODY_WINNER = "NOBODY"


def input_number(message):
    is_good_number = False
    number = 0

    while is_good_number == False:
        temp = input(message)

        if temp.isdigit() == True:
            number = int(temp)
            is_good_number = True
        else:
            print("Ошибка. Вы ввели не число")

    return number


def create_empty_field(battle_field):
    for i in range(ROWS):
        battle_field.append([])
        for j in range(COLS):
            battle_field[i].append(EMPTY_CELL)


def get_current_step():
    current_step = ""

    if random.randint(1, 1000) < 500:
        current_step = USER1_STEP
    else:
        current_step = USER2_STEP

    return current_step


def print_current_step(game_step):
    game_step += 1

    print()
    print("=============")
    print()

    print(f"Раунд {game_step}")
    print()

    return game_step


def print_battle_field(battle_field):
    print("Игровое поле: ")
    for i in range(ROWS):
        for j in range(COLS):
            print(battle_field[i][j], end=" ")
        print()

    print()


def make_step(battle_field, current_sign):
    print(f"Ход человека {current_sign}:")

    i_input = 0
    j_input = 0

    continue_input = True

    while continue_input == True:
        i_input = input_number("введите номер строки: ") - 1
        j_input = input_number("введите номер столбца: ") - 1

        if (
            i_input >= 0
            and i_input <= ROWS - 1
            and j_input >= 0
            and j_input <= COLS - 1
        ):
            if battle_field[i_input][j_input] == EMPTY_CELL:
                continue_input = False
            else:
                print("Ошибка. Эта клетка заполнена. Повторите снова")
        else:
            print("Ошибка ввода координат. Повторите снова")

    battle_field[i_input][j_input] = current_sign


def is_victory(battle_field, current_sign):
    victory = False

    if (
        # строки
        battle_field[0][0] == current_sign
        and battle_field[0][1] == current_sign
        and battle_field[0][2] == current_sign
        or battle_field[1][0] == current_sign
        and battle_field[1][1] == current_sign
        and battle_field[1][2] == current_sign
        or battle_field[2][0] == current_sign
        and battle_field[2][1] == current_sign
        and battle_field[2][2] == current_sign
        # столбцы
        or battle_field[0][0] == current_sign
        and battle_field[1][0] == current_sign
        and battle_field[2][0] == current_sign
        or battle_field[0][1] == current_sign
        and battle_field[1][1] == current_sign
        and battle_field[2][1] == current_sign
        or battle_field[0][2] == current_sign
        and battle_field[1][2] == current_sign
        and battle_field[2][2] == current_sign
        # диагонали
        or battle_field[0][0] == current_sign
        and battle_field[1][1] == current_sign
        and battle_field[2][2] == current_sign
        or battle_field[0][2] == current_sign
        and battle_field[1][1] == current_sign
        and battle_field[2][0] == current_sign
    ):
        victory = True

    return victory


def print_winner(winner):
    if winner == USER1_WINNER:
        print("Победил X")
    elif winner == USER2_WINNER:
        print("Победил O")
    elif winner == NOBODY_WINNER:
        print("Ничья")


def is_repeat_game():
    repeat_game = True

    print()

    repeat_answer = input(
        "Хотите сыграть ещё раз? Введите y - для повтора, n - для отказа: "
    )

    if repeat_answer == "n":
        repeat_game = False

    return repeat_game


repeat_game = True

while repeat_game == True:

    battle_field = []

    create_empty_field(battle_field)
    current_step = get_current_step()

    game_is_running = True
    winner = ""
    count_filled = 0
    game_step = 0

    while game_is_running == True:

        game_step = print_current_step(game_step)

        print_battle_field(battle_field)

        if current_step == USER1_STEP:
            make_step(battle_field, CRISS)
            current_step = USER2_STEP

        elif current_step == USER2_STEP:
            make_step(battle_field, CROSS)
            current_step = USER1_STEP

        count_filled += 1

        if is_victory(battle_field, CRISS) == True:
            winner = USER1_WINNER
            game_is_running = False
        elif is_victory(battle_field, CROSS) == True:
            winner = USER2_WINNER
            game_is_running = False
        elif count_filled == 9:
            winner = NOBODY_WINNER
            game_is_running = False

    print_current_step(game_step)

    print_battle_field(battle_field)

    print_winner(winner)

    repeat_game = is_repeat_game()
