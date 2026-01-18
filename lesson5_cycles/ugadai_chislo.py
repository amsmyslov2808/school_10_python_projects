import random

answer = ""

while answer != "no":
    print("Игра угадай число. Мухаха")
    print("Выберите уровень сложности")
    print("1. Легко")
    print("2. Средне")
    print("3. Сложно")
    print("4. Свои границы")
    difficulty_level = int(input("Введите уровень сложности: "))

    left_side = 0
    rigth_side = 0

    if difficulty_level == 1:
        print("Выбран лёгкий уровень сложности")
        left_side = 1
        rigth_side = 10
    elif difficulty_level == 2:
        print("Выбран средний уровень сложности")
        left_side = 1
        rigth_side = 50
    elif difficulty_level == 3:
        print("Выбран сложный уровень сложности")
        left_side = 1
        rigth_side = 100
    elif difficulty_level == 4:
        print("Выбран уровень сложности 'свои границы'")
        left_side = int(input("введите левую границу: "))
        rigth_side = int(input("введите правую границу: "))
    else:
        print("Выбран уровень сложности 'невероятные границы'")
        left_side = 1
        rigth_side = 1_000_000_000

    comp_number = random.randint(left_side, rigth_side + 1)
    user_number = 0

    count_tries = 0

    print(f"Я загадал число от {left_side} до {rigth_side}. Попробуй отгадай!")

    while user_number != comp_number:

        count_tries = count_tries + 1

        user_number = int(
            input(
                f"Попытка №{count_tries}. Введите своё число от {left_side} до {rigth_side}: "
            )
        )

        if user_number == 777:
            print(f"Пасхалка. Правильный ответ = {comp_number}")
            continue

        if user_number > comp_number:
            print("Введите поменьше")
            rigth_side = user_number - 1
        elif user_number < comp_number:
            print("Введите побольше")
            left_side = user_number + 1
        else:
            print("Вы угадали")

    if count_tries <= 5:
        print("Вы гений!")
    elif count_tries > 5 and count_tries <= 10:
        print("Неплохо!")
    elif count_tries > 10 and count_tries <= 15:
        print("Играй лучше!")
    else:
        print("Закрой игру и не открывай больше))))")

    answer = input("хотите сыграть в игру ещё раз? (yes/no): ")
