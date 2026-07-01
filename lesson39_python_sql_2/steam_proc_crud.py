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


@dataclass(slots=True)
class UserRole:
    role_name: str
    description: str
    id: int | None = None


@dataclass(slots=True)
class User:
    id: int
    nickname: str
    email: str
    steam_level: int
    hours_played: int
    last_online: datetime
    is_online: bool
    role_id: int

    role: UserRole | None = None

    def last_online_to_str(self):
        return self.last_online.strftime("%d.%m.%Y %H:%M:%S")

    def is_online_to_str(self):
        return "да" if self.is_online == True else "нет"


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def get_all_users_with_roles(conn) -> list[User]:
    users_list = []

    with conn.cursor(row_factory=dict_row) as cur:

        cur.execute(""" 
                    SELECT 
                    u.id,
                    u.nickname,
                    u.email,
                    u.steam_level, 
                    u.hours_played, 
                    u.last_online,
                    u.is_online,
                    u.role_id,

                    ur.id as ur_id,
                    ur.role_name,
                    ur.description

                    FROM users as u
                    JOIN user_roles as ur
                    ON u.role_id = ur.id

                    ORDER BY u.id ASC
                    """)

        rows = cur.fetchall()

        for row in rows:
            new_role = UserRole(row["ur_id"], row["role_name"], row["description"])

            new_user = User(
                id=row["id"],
                nickname=row["nickname"],
                email=row["email"],
                steam_level=row["steam_level"],
                hours_played=row["hours_played"],
                last_online=row["last_online"],
                is_online=row["is_online"],
                role_id=row["role_id"],
                role=new_role,
            )

            users_list.append(new_user)

    return users_list


def get_all_users(conn) -> list[User]:
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


def print_users_with_roles(users: list[User]):
    print("Пользователи:")

    print(
        f"{'ID':<5}{'NICKNAME':<20}{'EMAIL':<30}{'LEVEL':<10}{'HOURS':<10}{'LAST ONLINE':<22}{'ONLINE':<10}{'ROLE ID':<10}{'ROLE NAME':<15}{'DESCRIPTION'}"
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
            f"{user.role.role_name:<15}"
            f"{user.role.description}"
        )


def get_all_roles(conn) -> list[UserRole]:
    with conn.cursor(row_factory=class_row(UserRole)) as cur:

        cur.execute("""SELECT 
                    id, 
                    role_name,
                    description
                    FROM user_roles ORDER BY id ASC""")

        return list(cur.fetchall())


def print_roles(roles: list[UserRole]):
    print("Пользователи:")

    print(f"{'ID':<5}{'ROLE NAME':<15}{'DESCRIPTION':<50}")

    for role in roles:
        print(f"{role.id:<5}" f"{role.role_name:<15}" f"{role.description:<50}")


def add_new_role(conn, role: UserRole):
    with conn.cursor() as cur:
        cur.execute(
            """
                    INSERT INTO user_roles(
                    role_name, description)
                    VALUES (%s, %s)
                    """,
            (
                role.role_name,
                role.description,
            ),
        )
    conn.commit()


with get_connection() as conn:
    while True:
        users_with_roles = get_all_users_with_roles(conn)
        print_users_with_roles(users_with_roles)

        print("\n" + "*" * 50 + "\n")

        roles = get_all_roles(conn)
        print_roles(roles)

        print("\n" + "=" * 100 + "\n")

        input()

        add_new_role(conn, UserRole("новая роль", "новое описание"))
