# 1. создать поле общее для человека1 и человека2
# 2. заполнить поле пустотой
# 3. вывести поле на экран
# 4. рандомизируем право первого хода (крестик нолик)

# 5.1 ход человека1:
# ввести номер строки, ввести номер столбца для хода
# поставить в клетку по координатам крестик
# сделать проверку на победу

# 5.2 ход человека2:
# ввести номер строки, ввести номер столбца для хода
# поставить в клетку по координатам нолик
# сделать проверку на победу

import random

repeat_game = True

while repeat_game == True:

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

    battle_field = []

    for i in range(ROWS):
        battle_field.append([])
        for j in range(COLS):
            battle_field[i].append(EMPTY_CELL)

    current_step = ""
    if random.randint(1, 1000) < 500:
        current_step = USER1_STEP
    else:
        current_step = USER2_STEP

    game_is_running = True

    winner = ""

    count_filled = 0

    game_step = 0

    while game_is_running == True:

        game_step += 1

        print()
        print("=============")
        print()

        print(f"Раунд {game_step}")
        print()

        print("Игровое поле: ")
        for i in range(ROWS):
            for j in range(COLS):
                print(battle_field[i][j], end=" ")
            print()

        print()

        if current_step == USER1_STEP:
            print(f"Ход человека {CRISS}:")

            i_input = 0
            j_input = 0

            continue_input = True

            while continue_input == True:
                i_input = int(input("введите номер строки: ")) - 1
                j_input = int(input("введите номер столбца: ")) - 1

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

            battle_field[i_input][j_input] = CRISS

            current_step = USER2_STEP

            count_filled += 1

        elif current_step == USER2_STEP:
            print(f"Ход человека {CROSS}:")

            i_input = 0
            j_input = 0

            continue_input = True

            while continue_input == True:
                i_input = int(input("введите номер строки: ")) - 1
                j_input = int(input("введите номер столбца: ")) - 1

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

            battle_field[i_input][j_input] = CROSS

            current_step = USER1_STEP

            count_filled += 1

        if (
            # строки X
            battle_field[0][0] == CRISS
            and battle_field[0][1] == CRISS
            and battle_field[0][2] == CRISS
            or battle_field[1][0] == CRISS
            and battle_field[1][1] == CRISS
            and battle_field[1][2] == CRISS
            or battle_field[2][0] == CRISS
            and battle_field[2][1] == CRISS
            and battle_field[2][2] == CRISS
            # столбцы X
            or battle_field[0][0] == CRISS
            and battle_field[1][0] == CRISS
            and battle_field[2][0] == CRISS
            or battle_field[0][1] == CRISS
            and battle_field[1][1] == CRISS
            and battle_field[2][1] == CRISS
            or battle_field[0][2] == CRISS
            and battle_field[1][2] == CRISS
            and battle_field[2][2] == CRISS
            # диагонали X
            or battle_field[0][0] == CRISS
            and battle_field[1][1] == CRISS
            and battle_field[2][2] == CRISS
            or battle_field[0][2] == CRISS
            and battle_field[1][1] == CRISS
            and battle_field[2][0] == CRISS
        ):
            winner = USER1_WINNER
            game_is_running = False
        elif (
            # строки O
            battle_field[0][0] == CROSS
            and battle_field[0][1] == CROSS
            and battle_field[0][2] == CROSS
            or battle_field[1][0] == CROSS
            and battle_field[1][1] == CROSS
            and battle_field[1][2] == CROSS
            or battle_field[2][0] == CROSS
            and battle_field[2][1] == CROSS
            and battle_field[2][2] == CROSS
            # столбцы O
            or battle_field[0][0] == CROSS
            and battle_field[1][0] == CROSS
            and battle_field[2][0] == CROSS
            or battle_field[0][1] == CROSS
            and battle_field[1][1] == CROSS
            and battle_field[2][1] == CROSS
            or battle_field[0][2] == CROSS
            and battle_field[1][2] == CROSS
            and battle_field[2][2] == CROSS
            # диагонали O
            or battle_field[0][0] == CROSS
            and battle_field[1][1] == CROSS
            and battle_field[2][2] == CROSS
            or battle_field[0][2] == CROSS
            and battle_field[1][1] == CROSS
            and battle_field[2][0] == CROSS
        ):
            winner = USER2_WINNER
            game_is_running = False
        elif count_filled == 9:
            winner = NOBODY_WINNER
            game_is_running = False

    print()
    print("=============")
    print()

    print(f"Раунд {game_step}")
    print()

    print("Игровое поле: ")
    for i in range(ROWS):
        for j in range(COLS):
            print(battle_field[i][j], end=" ")
        print()
    print()

    if winner == USER1_WINNER:
        print("Победил X")
    elif winner == USER2_WINNER:
        print("Победил O")
    elif winner == NOBODY_WINNER:
        print("Ничья")

    print()

    repeat_answer = input(
        "Хотите сыграть ещё раз? Введите y - для повтора, n - для отказа: "
    )

    if repeat_answer == "n":
        repeat_game = False
