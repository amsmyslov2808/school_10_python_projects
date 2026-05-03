from participant import Participant
from capitain import Capitain
from tournament import Tournament
from decorators import log_action


@log_action
def add_standart_participants(tournament: Tournament):
    name = input("Введите имя:")
    clas = input("Введите класс:")
    participant = Participant(name=name, school_class=clas)
    tournament.add_participant(participant)


@log_action
def add_capitain_participants(tournament: Tournament):
    name = input("Введите имя:")
    clas = input("Введите класс:")
    team = input("Введите название команды:")
    capitain = Capitain(name=name, school_class=clas, team_name=team)
    tournament.add_participant(capitain)


tournament = Tournament()

while True:
    print("=== Школьный турнир знаний ===")
    print()
    print("1. Добавить обычного участника")
    print("2. Добавить капитана")
    print("3. Показать всех участников")
    print("4. Начислить баллы участнику")
    print("5. Снять баллы с участника")
    print("6. Показать рейтинг")
    print("7. Показать __dict__ участников")
    print("8. Удалить участника *")
    print("9. Показать победителя *")
    print("9. Показать победителя *")
    print("0. Выйти")
    key = input()
    if key == "1":
        add_standart_participants(tournament)
    elif key == "2":
        add_capitain_participants(tournament)
    elif key == "3":
        for participant in tournament._participants:
            print(participant)
    elif key == "4":
        name = input("Введите имя участника: ")
        points = int(input("Введите количество баллов: "))
        tournament.add_points_to_parcticipant(name, points)
        if tournament.find_participant(name).get_role == "Участник":
            print(f"{name} начислено {points} баллов")
        else:
            print(f"{name} начислено {points+2} баллов с учётом бонуса капитана.")
    elif key == "5":
        name = input("Введите имя участника: ")
        points = int(input("Введите количество баллов: "))

        fp = tournament.find_participant(name)

        print(f"Было: {fp._points}")
        print(f"Снимаем: {points}")
        if points > fp._points:
            points = fp._points
        tournament.remove_points_to_participant(name, points)
        print(f"Стало: {fp._points}")
    elif key == "6":
        tournament.show_rating()
    elif key == "7":
        tournament.show_debug_info()
    elif key == "8":
        name = input()
        try:
            del tournament[tournament.find_participant(name)]
        except:
            print("Участник не найден.")
    elif key == "9":
        try:
            print(tournament.get_winner())
        except:
            print("Победителя пока нет, потому что список участников пуст.")
    elif key == "0":
        break
