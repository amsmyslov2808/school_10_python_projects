from tamagotchi import Tamagotchi
import console_services

tamagotchi_name: str = console_services.input_str(
    "введите имя своего Тамагочи: ", 2, 30
)
tamagotchi_type_animal: str = console_services.input_str(
    "введите тип животного для своего Тамагочи: ", 2, 30
)
tamagotchi_age: int = console_services.input_int(
    "введите возраст своего Тамагочи: ", 0, 1000
)

tamagotchi = Tamagotchi(tamagotchi_name, tamagotchi_type_animal, tamagotchi_age)
current_day = 0

print(
    "Игра начинается. Ваша задача чтобы Тамагочи прожил как можно больше дней. Если хоть один из параметров Тамагочи достигнет нуля он проиграет"
    + "\n"
    + "\n"
)

while tamagotchi.is_alive():
    # console_services.clear_console()

    current_day += 1
    print(f"{current_day} день Тамагочи")
    console_services.print_devider()

    tamagotchi.print_status()
    console_services.print_devider()

    tamagotchi.reset_params_changes()

    print("Выберите действие с вашим Тамагочи")
    print("1. Покормить")
    print("2. Поиграть")
    print("3. Уложить спать")

    action = console_services.input_int("введите число от 1 до 3: ", 1, 3)

    if action == 1:
        tamagotchi.feed()
    elif action == 2:
        tamagotchi.play()
    elif action == 3:
        tamagotchi.sleep()

    tamagotchi.normalized_parameters()

    tamagotchi.random_event()

    tamagotchi.print_params_changes()

    console_services.check_enter()
