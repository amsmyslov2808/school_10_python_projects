import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "school_crud",
    "user": "postgres",
    "password": "12345",
}


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def show_teams(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, name, city
            FROM teams
            ORDER BY id;
        """)

        teams = cur.fetchall()

    print("\nКоманды:")
    for team in teams:
        print(f"{team[0]}. {team[1]} — {team[2]}")


def show_players(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                p.id,
                p.nickname,
                p.age,
                p.rating,
                p.coins,
                t.name AS team_name
            FROM players AS p
            LEFT JOIN teams AS t
            ON p.team_id = t.id
            ORDER BY p.id;
        """)

        players = cur.fetchall()

    print("\nИгроки:")
    for player in players:
        team_name = player[5] if player[5] is not None else "без команды"

        print(
            f"{player[0]}. {player[1]} | "
            f"возраст: {player[2]} | "
            f"рейтинг: {player[3]} | "
            f"монеты: {player[4]} | "
            f"команда: {team_name}"
        )


def add_player(conn):
    print("\nДобавление игрока")

    nickname = input("Никнейм: ")
    age = int(input("Возраст: "))
    rating = float(input("Рейтинг от 0 до 5: "))
    coins = int(input("Монеты: "))

    show_teams(conn)
    team_id_text = input("ID команды или Enter, если без команды: ")

    if team_id_text == "":
        team_id = None
    else:
        team_id = int(team_id_text)

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO players (nickname, age, rating, coins, team_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """,
            (nickname, age, rating, coins, team_id),
        )

        new_id = cur.fetchone()[0]

    conn.commit()

    print(f"Игрок добавлен. ID нового игрока: {new_id}")


def update_player_rating(conn):
    print("\nИзменение рейтинга игрока")

    player_id = int(input("ID игрока: "))
    new_rating = float(input("Новый рейтинг от 0 до 5: "))

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE players
            SET rating = %s
            WHERE id = %s;
        """,
            (new_rating, player_id),
        )

        changed_rows = cur.rowcount

    conn.commit()

    if changed_rows == 0:
        print("Игрок с таким ID не найден.")
    else:
        print("Рейтинг игрока обновлён.")


def update_player_team(conn):
    print("\nПеревод игрока в другую команду")

    player_id = int(input("ID игрока: "))

    show_teams(conn)
    team_id_text = input("Новый ID команды или Enter, чтобы убрать команду: ")

    if team_id_text == "":
        team_id = None
    else:
        team_id = int(team_id_text)

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE players
            SET team_id = %s
            WHERE id = %s;
        """,
            (team_id, player_id),
        )

        changed_rows = cur.rowcount

    conn.commit()

    if changed_rows == 0:
        print("Игрок с таким ID не найден.")
    else:
        print("Команда игрока обновлена.")


def delete_player(conn):
    print("\nУдаление игрока")

    player_id = int(input("ID игрока: "))

    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM players
            WHERE id = %s;
        """,
            (player_id,),
        )

        changed_rows = cur.rowcount

    conn.commit()

    if changed_rows == 0:
        print("Игрок с таким ID не найден.")
    else:
        print("Игрок удалён.")


def search_players(conn):
    print("\nПоиск игроков")

    text = input("Введите часть никнейма: ")

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, nickname, age, rating, coins
            FROM players
            WHERE nickname ILIKE %s
            ORDER BY nickname;
        """,
            (f"%{text}%",),
        )

        players = cur.fetchall()

    if len(players) == 0:
        print("Игроки не найдены.")
        return

    for player in players:
        print(
            f"{player[0]}. {player[1]} | "
            f"возраст: {player[2]} | "
            f"рейтинг: {player[3]} | "
            f"монеты: {player[4]}"
        )


def print_menu():
    print("\n--- CRUD Players ---")
    print("1. Показать всех игроков")
    print("2. Показать команды")
    print("3. Добавить игрока")
    print("4. Изменить рейтинг игрока")
    print("5. Перевести игрока в другую команду")
    print("6. Удалить игрока")
    print("7. Найти игрока по никнейму")
    print("0. Выход")


def main():
    conn = get_connection()

    try:
        while True:
            print_menu()

            command = input("Выберите действие: ")

            if command == "1":
                show_players(conn)
            elif command == "2":
                show_teams(conn)
            elif command == "3":
                add_player(conn)
            elif command == "4":
                update_player_rating(conn)
            elif command == "5":
                update_player_team(conn)
            elif command == "6":
                delete_player(conn)
            elif command == "7":
                search_players(conn)
            elif command == "0":
                print("Программа завершена.")
                break
            else:
                print("Неизвестная команда.")

    except Exception as error:
        conn.rollback()
        print("Ошибка:", error)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
