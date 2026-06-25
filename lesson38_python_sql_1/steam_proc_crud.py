import psycopg
from psycopg.rows import dict_row

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


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def get_users(conn) -> list[User]:
    users_list = []
    users_from_db = None

    with conn.cursor(row_factory=dict_row) as cur:

        cur.execute("SELECT * FROM users ORDER BY id ASC")

        users_from_db = cur.fetchall()

    for user in users_from_db:
        new_user = User(
            id=user["id"],
            nickname=user["nickname"],
            email=user["email"],
            steam_level=user["steam_level"],
            hours_played=user["hours_played"],
            last_online=user["last_online"],
            is_online=user["is_online"],
            role_id=user["role_id"],
        )

        users_list.append(new_user)

    return users_list


def print_users(users: list[User]):
    print("Пользователи:")

    print(
        f"{'ID':<5}{'NICKNAME':<20}{'EMAIL':<30}{'LEVEL':<10}{'HOURS':<10}{'LAST ONLINE':<22}{'ONLINE':<10}{'ROLE ID':<10}"
    )

    for user in users:

        last_online_text = user.last_online.strftime("%d.%m.%Y %H:%M:%S")

        if user.is_online == True:
            online_text = "да"
        else:
            online_text = "нет"

        print(
            f"{user.id:<5}"
            f"{user.nickname:<20}"
            f"{user.email:<30}"
            f"{user.steam_level:<10}"
            f"{user.hours_played:<10}"
            f"{last_online_text:<22}"
            f"{online_text:<10}"
            f"{user.role_id:<10}"
        )


conn = get_connection()

users = get_users(conn)


print_users(users)

conn.close()
