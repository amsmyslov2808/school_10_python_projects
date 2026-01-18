# # 1. создать поле человека 10х10 клеток
# # 2. создать поле компьютера 10х10 клеток
# # 3. расставить рандомно корабли (10 шт.) на обоих полях
# # 4. вывести поля человека и компьютера на экран (на поле компьютера вместа корабля показывать знак пустой клетки)
# # 5. рандомизируем право первого хода

# # 6.1 ход человека:
# # ввести номер строки, ввести номер столбца для выстрела
# # сделать проверку, что клетка с этими коорднитами находится в поле, что в неё не стреляли раньше
# # проверка на попадание игрока в корабль противника, если попал то клетка с кораблём помечается как убитый корабль и ход остаётся человеку, если не попал то клетка помечается как промах и ход переходит к компьютеру
# # если было попадаение делать провеку на количество оставшихся кораблей у компьютера, если оно = 0, то выиграл человек

# # 6.2 ход компьютера:
# # срандомить номер строки, ввести номер столбца для выстрела
# # сделать проверку что в клетку не стреляли раньше
# # проверка на попадание компьютера в корабль противника, если попал то клетка с кораблём помечается как убитый корабль и ход остаётся компьютеру, если не попал то клетка помечается как промах и ход переходит к человеку
# # если было попадаение делать провеку на количество оставшихся кораблей у человека, если оно = 0, то выиграл компьютер

import random

repeat_game = True

while repeat_game == True:

    ALIVE_SHIP = "K"
    DEAD_SHIP = "X"
    MISS_CELL = "O"
    EMPTY_CELL = "."

    COLS = 2
    ROWS = 2

    COUNT_SHIPS = 2

    USER_STEP = "USER"
    COMP_STEP = "COMP"

    USER_WINNER = "USER"
    COMP_WINNER = "COMP"

    user_field = []
    comp_field = []

    for i in range(ROWS):
        user_field.append([])
        for j in range(COLS):
            user_field[i].append(EMPTY_CELL)

    for i in range(ROWS):
        comp_field.append([])
        for j in range(COLS):
            comp_field[i].append(EMPTY_CELL)

    for _ in range(COUNT_SHIPS):
        continue_random = True
        i_rand = 0
        j_rand = 0
        while continue_random == True:
            i_rand = random.randint(0, ROWS - 1)
            j_rand = random.randint(0, COLS - 1)

            if user_field[i_rand][j_rand] == EMPTY_CELL:
                user_field[i_rand][j_rand] = ALIVE_SHIP
                continue_random = False

    for _ in range(COUNT_SHIPS):
        continue_random = True
        i_rand = 0
        j_rand = 0
        while continue_random == True:
            i_rand = random.randint(0, ROWS - 1)
            j_rand = random.randint(0, COLS - 1)

            if comp_field[i_rand][j_rand] == EMPTY_CELL:
                comp_field[i_rand][j_rand] = ALIVE_SHIP
                continue_random = False

    current_step = ""
    if random.randint(1, 1000) < 500:
        current_step = USER_STEP
    else:
        current_step = COMP_STEP

    game_is_running = True

    user_alive_ships = COUNT_SHIPS
    comp_alive_ships = COUNT_SHIPS

    winner = ""

    game_step = 0

    while game_is_running == True:

        game_step += 1

        print()
        print("=============")
        print()

        print(f"Раунд {game_step}")
        print()

        print("Поле человека: ")
        for i in range(ROWS):
            for j in range(COLS):
                print(user_field[i][j], end=" ")
            print()

        print("Поле компьютера: ")
        for i in range(ROWS):
            for j in range(COLS):
                if comp_field[i][j] == ALIVE_SHIP:
                    print(EMPTY_CELL, end=" ")
                else:
                    print(comp_field[i][j], end=" ")
            print()

        print()

        if current_step == USER_STEP:
            print("Ход человека:")
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
                    if (
                        comp_field[i_input][j_input] == ALIVE_SHIP
                        or comp_field[i_input][j_input] == EMPTY_CELL
                    ):
                        continue_input = False
                    else:
                        print("Ошибка. Вы уже стреляли в эту клетку. Повторите снова")
                else:
                    print("Ошибка ввода координат. Повторите снова")

            if comp_field[i_input][j_input] == ALIVE_SHIP:
                comp_field[i_input][j_input] = DEAD_SHIP
                comp_alive_ships -= 1
                print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - убит")
                print(f"У противника осталось кораблей: {comp_alive_ships}")

                if comp_alive_ships == 0:
                    game_is_running = False
                    winner = USER_WINNER

            elif comp_field[i_input][j_input] == EMPTY_CELL:
                comp_field[i_input][j_input] = MISS_CELL
                current_step = COMP_STEP

                print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - промах")
                print(f"У противника осталось кораблей: {comp_alive_ships}")

        elif current_step == COMP_STEP:
            input("Ход компьютера (нажмите Enter для продолжения):")

            i_input = 0
            j_input = 0

            continue_input = True

            while continue_input == True:
                i_input = random.randint(0, ROWS - 1)
                j_input = random.randint(0, COLS - 1)

                if (
                    user_field[i_input][j_input] == ALIVE_SHIP
                    or user_field[i_input][j_input] == EMPTY_CELL
                ):
                    continue_input = False

            if user_field[i_input][j_input] == ALIVE_SHIP:
                user_field[i_input][j_input] = DEAD_SHIP
                user_alive_ships -= 1

                print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - убит")
                print(f"У человека осталось кораблей: {user_alive_ships}")
                input("Нажмите Enter для продолжения")

                if user_alive_ships == 0:
                    game_is_running = False
                    winner = COMP_WINNER

            elif user_field[i_input][j_input] == EMPTY_CELL:
                user_field[i_input][j_input] = MISS_CELL
                current_step = USER_STEP

                print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - промах")
                print(f"У человека осталось кораблей: {user_alive_ships}")
                input("Нажмите Enter для продолжения")

    print()
    print("=============")
    print()

    print(f"Раунд {game_step}")
    print()

    print("Поле человека: ")
    for i in range(ROWS):
        for j in range(COLS):
            print(user_field[i][j], end=" ")
        print()

    print("Поле компьютера: ")
    for i in range(ROWS):
        for j in range(COLS):
            if comp_field[i][j] == ALIVE_SHIP:
                print(EMPTY_CELL, end=" ")
            else:
                print(comp_field[i][j], end=" ")
        print()

    print()

    if winner == USER_WINNER:
        print("Победил пользователь")
    elif winner == COMP_WINNER:
        print("Победил компьютер")

    print()

    repeat_answer = input(
        "Хотите сыграть ещё раз? Введите y - для повтора, n - для отказа: "
    )

    if repeat_answer == "n":
        repeat_game = False
