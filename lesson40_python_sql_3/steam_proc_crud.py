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
    nickname: str
    email: str
    steam_level: int
    hours_played: int
    last_online: datetime
    is_online: bool
    role_id: int

    id: int | None = None

    role: UserRole | None = None

    def last_online_to_str(self):
        return self.last_online.strftime("%d.%m.%Y %H:%M:%S")

    def is_online_to_str(self):
        return "да" if self.is_online == True else "нет"


def get_connection():
    return psycopg.connect(**DB_CONFIG)


# ===== USERS START =====


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
            new_role = UserRole(
                id=row["ur_id"],
                role_name=row["role_name"],
                description=row["description"],
            )

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


# ===== USERS FINISH =====

# ===== ROLES START =====


def get_all_roles(conn) -> list[UserRole]:
    with conn.cursor(row_factory=class_row(UserRole)) as cur:

        cur.execute("""
                    SELECT 
                    id, 
                    role_name,
                    description
                    FROM user_roles ORDER BY id ASC
                    """)

        return list(cur.fetchall())


def get_role_by_id(conn, id: int) -> UserRole | None:
    with conn.cursor(row_factory=class_row(UserRole)) as cur:
        cur.execute(
            """
                    SELECT 
                    id, 
                    role_name,
                    description
                    FROM user_roles 
                    WHERE id = %s
                    """,
            (id,),
        )

        return cur.fetchone()


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


def update_role_by_id(conn, role: UserRole) -> bool:
    with conn.cursor() as cur:
        cur.execute(
            """
                    UPDATE user_roles
	                SET role_name=%s, description=%s
	                WHERE id=%s
                    """,
            (
                role.role_name,
                role.description,
                role.id,
            ),
        )

        updated_rows = cur.rowcount

    conn.commit()

    return updated_rows != 0


def delete_role_by_id(conn, id: int):
    with conn.cursor() as cur:
        cur.execute(
            """
                    DELETE FROM user_roles
                    WHERE id = %s
                    """,
            (id,),
        )
    conn.commit()


def print_one_role(role: UserRole):
    print(f"{role.id:<5}" f"{role.role_name:<15}" f"{role.description:<50}")


def print_roles_table_header():
    print(f"{'ID':<5}{'ROLE NAME':<15}{'DESCRIPTION':<50}")


def print_roles(roles: list[UserRole]):
    print("Пользователи:")

    print_roles_table_header()

    for role in roles:
        print_one_role(role)


# ===== USERS FINISH =====

with get_connection() as conn:

    is_run = True

    while is_run == True:
        try:
            users_with_roles = get_all_users_with_roles(conn)
            print_users_with_roles(users_with_roles)

            print("\n" + "*" * 50 + "\n")

            roles = get_all_roles(conn)
            print_roles(roles)

            print("\n" + "=" * 100 + "\n")

            print("Меню:")
            print("1. Вывести роль по id")
            print("2. Добавить новую роль")
            print("3. Удалить роль по id")
            print("4. Обновить роль по id")

            print("0. Выход")

            menu_number = int(input("выберите пункт меню: "))

            if menu_number == 1:
                id = int(input("введите id роли: "))
                role = get_role_by_id(conn, id)

                print_roles_table_header()

                if role == None:
                    print(f"Роль с id {id} не найдена")
                else:
                    print_one_role(role)

            elif menu_number == 2:
                role_name = input("введите название роли: ")
                description = input("введите описание роли: ")

                add_new_role(
                    conn, UserRole(role_name=role_name, description=description)
                )
            elif menu_number == 3:
                id = int(input("введите id роли: "))

                delete_role_by_id(conn, id)

                print("успешно удалено")
            elif menu_number == 4:

                id = int(input("введите id роли: "))
                role_name = input("введите название роли: ")
                description = input("введите описание роли: ")

                is_update = update_role_by_id(
                    conn, UserRole(id=id, role_name=role_name, description=description)
                )

                if is_update == True:
                    print("успешно обновлено")
                else:
                    print(f"роль c id {id} не найдена")
            elif menu_number == 0:
                is_run = False

            input("\n\n\nдля продолжения нажмите <Enter>\n\n\n")
        except Exception as e:
            print(
                f"Ошибка в работе с программой. Кратко: {str(e)}. Подробно: {repr(e)}"
            )
            is_run = False
