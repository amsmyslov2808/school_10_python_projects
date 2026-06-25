import psycopg

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "school_crud",
    "user": "postgres",
    "password": "12345",
}


class Database:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        self.conn = psycopg.connect(**self.config)

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def fetch_all(self, sql, params=None):
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def fetch_one(self, sql, params=None):
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()

    def execute(self, sql, params=None):
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.rowcount


class Player:
    def __init__(self, player_id, nickname, age, rating, coins, team_name):
        self.id = player_id
        self.nickname = nickname
        self.age = age
        self.rating = rating
        self.coins = coins
        self.team_name = team_name

    def print_info(self):
        team = self.team_name if self.team_name is not None else "без команды"

        print(
            f"{self.id}. {self.nickname} | "
            f"возраст: {self.age} | "
            f"рейтинг: {self.rating} | "
            f"монеты: {self.coins} | "
            f"команда: {team}"
        )


class PlayerRepository:
    def __init__(self, database):
        self.database = database

    def get_all(self):
        rows = self.database.fetch_all("""
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

        players = []

        for row in rows:
            player = Player(
                player_id=row[0],
                nickname=row[1],
                age=row[2],
                rating=row[3],
                coins=row[4],
                team_name=row[5],
            )

            players.append(player)

        return players

    def search_by_nickname(self, text):
        rows = self.database.fetch_all(
            """
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
            WHERE p.nickname ILIKE %s
            ORDER BY p.nickname;
        """,
            (f"%{text}%",),
        )

        players = []

        for row in rows:
            players.append(
                Player(
                    player_id=row[0],
                    nickname=row[1],
                    age=row[2],
                    rating=row[3],
                    coins=row[4],
                    team_name=row[5],
                )
            )

        return players

    def create(self, nickname, age, rating, coins, team_id):
        row = self.database.fetch_one(
            """
            INSERT INTO players (nickname, age, rating, coins, team_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """,
            (nickname, age, rating, coins, team_id),
        )

        self.database.commit()

        return row[0]

    def update_rating(self, player_id, new_rating):
        changed_rows = self.database.execute(
            """
            UPDATE players
            SET rating = %s
            WHERE id = %s;
        """,
            (new_rating, player_id),
        )

        self.database.commit()

        return changed_rows

    def update_team(self, player_id, team_id):
        changed_rows = self.database.execute(
            """
            UPDATE players
            SET team_id = %s
            WHERE id = %s;
        """,
            (team_id, player_id),
        )

        self.database.commit()

        return changed_rows

    def delete(self, player_id):
        changed_rows = self.database.execute(
            """
            DELETE FROM players
            WHERE id = %s;
        """,
            (player_id,),
        )

        self.database.commit()

        return changed_rows


class TeamRepository:
    def __init__(self, database):
        self.database = database

    def get_all(self):
        return self.database.fetch_all("""
            SELECT id, name, city
            FROM teams
            ORDER BY id;
        """)


class ConsoleApp:
    def __init__(self, player_repository, team_repository):
        self.player_repository = player_repository
        self.team_repository = team_repository

    def run(self):
        while True:
            self.print_menu()

            command = input("Выберите действие: ")

            if command == "1":
                self.show_players()
            elif command == "2":
                self.show_teams()
            elif command == "3":
                self.add_player()
            elif command == "4":
                self.update_player_rating()
            elif command == "5":
                self.update_player_team()
            elif command == "6":
                self.delete_player()
            elif command == "7":
                self.search_players()
            elif command == "0":
                print("Программа завершена.")
                break
            else:
                print("Неизвестная команда.")

    def print_menu(self):
        print("\n--- CRUD Players OOP ---")
        print("1. Показать всех игроков")
        print("2. Показать команды")
        print("3. Добавить игрока")
        print("4. Изменить рейтинг игрока")
        print("5. Перевести игрока в другую команду")
        print("6. Удалить игрока")
        print("7. Найти игрока по никнейму")
        print("0. Выход")

    def show_players(self):
        players = self.player_repository.get_all()

        print("\nИгроки:")

        for player in players:
            player.print_info()

    def show_teams(self):
        teams = self.team_repository.get_all()

        print("\nКоманды:")

        for team in teams:
            print(f"{team[0]}. {team[1]} — {team[2]}")

    def add_player(self):
        print("\nДобавление игрока")

        nickname = input("Никнейм: ")
        age = int(input("Возраст: "))
        rating = float(input("Рейтинг от 0 до 5: "))
        coins = int(input("Монеты: "))

        self.show_teams()

        team_id_text = input("ID команды или Enter, если без команды: ")

        if team_id_text == "":
            team_id = None
        else:
            team_id = int(team_id_text)

        new_id = self.player_repository.create(
            nickname=nickname, age=age, rating=rating, coins=coins, team_id=team_id
        )

        print(f"Игрок добавлен. ID нового игрока: {new_id}")

    def update_player_rating(self):
        print("\nИзменение рейтинга игрока")

        player_id = int(input("ID игрока: "))
        new_rating = float(input("Новый рейтинг от 0 до 5: "))

        changed_rows = self.player_repository.update_rating(player_id, new_rating)

        if changed_rows == 0:
            print("Игрок с таким ID не найден.")
        else:
            print("Рейтинг игрока обновлён.")

    def update_player_team(self):
        print("\nПеревод игрока в другую команду")

        player_id = int(input("ID игрока: "))

        self.show_teams()

        team_id_text = input("Новый ID команды или Enter, чтобы убрать команду: ")

        if team_id_text == "":
            team_id = None
        else:
            team_id = int(team_id_text)

        changed_rows = self.player_repository.update_team(player_id, team_id)

        if changed_rows == 0:
            print("Игрок с таким ID не найден.")
        else:
            print("Команда игрока обновлена.")

    def delete_player(self):
        print("\nУдаление игрока")

        player_id = int(input("ID игрока: "))

        changed_rows = self.player_repository.delete(player_id)

        if changed_rows == 0:
            print("Игрок с таким ID не найден.")
        else:
            print("Игрок удалён.")

    def search_players(self):
        print("\nПоиск игроков")

        text = input("Введите часть никнейма: ")

        players = self.player_repository.search_by_nickname(text)

        if len(players) == 0:
            print("Игроки не найдены.")
            return

        for player in players:
            player.print_info()


def main():
    database = Database(DB_CONFIG)

    try:
        database.connect()

        player_repository = PlayerRepository(database)
        team_repository = TeamRepository(database)

        app = ConsoleApp(player_repository, team_repository)
        app.run()

    except Exception as error:
        database.rollback()
        print("Ошибка:", error)

    finally:
        database.close()


if __name__ == "__main__":
    main()
