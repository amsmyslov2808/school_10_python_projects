import psycopg
from psycopg.rows import dict_row, class_row

from dataclasses import dataclass
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "steam_db",
    "user": "postgres",
    "password": "12345",
}


@dataclass
class User:
    id: int
    nickname: str
    email: str
    steam_level: int
    hours_played: int
    last_online: datetime
    is_online: bool
    role_id: int

    def last_online_to_str(self):
        return self.last_online.strftime("%d.%m.%Y %H:%M:%S")

    def is_online_to_str(self):
        return "да" if self.is_online == True else "нет"


def get_connection():
    return psycopg.connect(**DB_CONFIG)


# def get_users(conn) -> list[User]:
#     users_list = []
#     users_from_db = None

#     with conn.cursor(row_factory=dict_row) as cur:

#         cur.execute("SELECT * FROM users ORDER BY id ASC")

#         users_from_db = cur.fetchall()

#     for user in users_from_db:
#         new_user = User(
#             id=user["id"],
#             nickname=user["nickname"],
#             email=user["email"],
#             steam_level=user["steam_level"],
#             hours_played=user["hours_played"],
#             last_online=user["last_online"],
#             is_online=user["is_online"],
#             role_id=user["role_id"],
#         )

#         users_list.append(new_user)

#     return users_list


def get_users(conn) -> list[User]:
    with conn.cursor(row_factory=class_row(User)) as cur:

        cur.execute("""SELECT 
                    id, 
                    nickname, 
                    email, 
                    steam_level, 
                    hours_played,
                    last_online,
                    is_online,
                    role_id
                    FROM users ORDER BY id ASC""")

        return list(cur.fetchall())


def print_users(users: list[User]):
    print("Пользователи:")

    print(
        f"{'ID':<5}{'NICKNAME':<20}{'EMAIL':<30}{'LEVEL':<10}{'HOURS':<10}{'LAST ONLINE':<22}{'ONLINE':<10}{'ROLE ID':<10}"
    )

    for user in users:

        print(
            f"{user.id:<5}"
            f"{user.nickname:<20}"
            f"{user.email:<30}"
            f"{user.steam_level:<10}"
            f"{user.hours_played:<10}"
            f"{user.last_online_to_str():<22}"
            f"{user.is_online_to_str():<10}"
            f"{user.role_id:<10}"
        )


with get_connection() as conn:

    users = get_users(conn)

    print_users(users)
