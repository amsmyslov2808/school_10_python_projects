from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    select,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    joinedload,
    mapped_column,
    relationship,
    sessionmaker,
)

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/steam_db"


class Base(DeclarativeBase):
    pass


class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)

    users: Mapped[list["User"]] = relationship(back_populates="role")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    steam_level: Mapped[int] = mapped_column(Integer, nullable=False)
    hours_played: Mapped[int] = mapped_column(Integer, nullable=False)
    last_online: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_online: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user_roles.id", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
    )

    role: Mapped[UserRole] = relationship(back_populates="users")

    def last_online_to_str(self):
        return self.last_online.strftime("%d.%m.%Y %H:%M:%S")

    def is_online_to_str(self):
        return "да" if self.is_online == True else "нет"


engine = create_engine(DATABASE_URL, echo=True)

get_session_local = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


def get_all_users_with_roles(session: Session) -> list[User]:
    query = select(User).options(joinedload(User.role)).order_by(User.id)

    return list(session.scalars(query).all())


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
    query = select(UserRole).order_by(UserRole.id)

    return list(session.scalars(query).all())


def print_one_role(role: UserRole):
    print(f"{role.id:<5}" f"{role.role_name:<15}" f"{role.description:<50}")


def print_roles_table_header():
    print(f"{'ID':<5}{'ROLE NAME':<15}{'DESCRIPTION':<50}")


def print_roles(roles: list[UserRole]):
    print("Роли:")

    print_roles_table_header()

    for role in roles:
        print_one_role(role)


with get_session_local() as session:
    is_run = True

    while is_run == True:
        try:
            users_with_roles = get_all_users_with_roles(session)
            print_users_with_roles(users_with_roles)

            print("\n" + "*" * 50 + "\n")

            roles = get_all_roles(session)
            print_roles(roles)

            print("\n" + "=" * 100 + "\n")

            print("Меню:")
            print("1. Вывести роль по id")
            print("2. Добавить новую роль")
            print("3. Удалить роль по id")
            print("4. Обновить роль по id")

            print("5. Вывести пользователя по id")
            print("6. Добавить нового пользователя")
            print("7. Удалить пользователя по id")
            print("8. Обновить пользователя по id")

            print("0. Выход")

            menu_number = int(input("выберите пункт меню: "))

            # if menu_number == 1:
            #     id = int(input("введите id роли: "))
            #     role = get_role_by_id(conn, id)

            #     print_roles_table_header()

            #     if role == None:
            #         print(f"Роль с id {id} не найдена")
            #     else:
            #         print_one_role(role)

        #     elif menu_number == 2:
        #         role_name = input("введите название роли: ")
        #         description = input("введите описание роли: ")

        #         add_new_role(
        #             conn, UserRole(role_name=role_name, description=description)
        #         )

        #         print("успешно добавлено")
        #     elif menu_number == 3:
        #         id = int(input("введите id роли: "))

        #         delete_role_by_id(conn, id)

        #         print("успешно удалено")
        #     elif menu_number == 4:

        #         id = int(input("введите id роли: "))
        #         role_name = input("введите название роли: ")
        #         description = input("введите описание роли: ")

        #         is_update = update_role_by_id(
        #             conn, UserRole(id=id, role_name=role_name, description=description)
        #         )

        #         if is_update == True:
        #             print("успешно обновлено")
        #         else:
        #             print(f"роль c id {id} не найдена")
        #     elif menu_number == 5:
        #         id = int(input("введите id пользователя: "))

        #         user = get_user_by_id(conn, id)

        #         print_users_table_header()

        #         if user == None:
        #             print(f"Пользователь с id {id} не найден")
        #         else:
        #             print_one_user(user)
        #     elif menu_number == 6:
        #         nickname = input("Никнейм: ")
        #         email = input("Email: ")
        #         steam_level = int(input("Уровень Steam: "))
        #         hours_played = int(input("Часы: "))

        #         # Формат ввода даты: ГГГГ-ММ-ДД ЧЧ:ММ:СС (например, 2026-07-08 14:30:00)
        #         last_online = datetime.fromisoformat(
        #             input("Последний онлайн (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
        #         )

        #         # Ввод True/False (любая непустая строка станет True, пустой Enter станет False)
        #         is_online = bool(
        #             input(
        #                 "В сети? (Нажмите Enter если нет, введите любой символ если да): "
        #             )
        #         )
        #         role_id = int(input("ID роли: "))

        #         add_new_user(
        #             conn,
        #             user=User(
        #                 nickname=nickname,
        #                 email=email,
        #                 steam_level=steam_level,
        #                 hours_played=hours_played,
        #                 last_online=last_online,
        #                 is_online=is_online,
        #                 role_id=role_id,
        #             ),
        #         )

        #         print("успешно добавлено")
        #     elif menu_number == 7:
        #         id = int(input("введите id роли: "))

        #         delete_user_by_id(conn, id)

        #         print("успешно удалено")
        #     elif menu_number == 8:
        #         id = int(input("введите id пользователя: "))

        #         nickname = input("Никнейм: ")
        #         email = input("Email: ")
        #         steam_level = int(input("Уровень Steam: "))
        #         hours_played = int(input("Часы: "))

        #         # Формат ввода даты: ГГГГ-ММ-ДД ЧЧ:ММ:СС (например, 2026-07-08 14:30:00)
        #         last_online = datetime.fromisoformat(
        #             input("Последний онлайн (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
        #         )

        #         # Ввод True/False (любая непустая строка станет True, пустой Enter станет False)
        #         is_online = bool(
        #             input(
        #                 "В сети? (Нажмите Enter если нет, введите любой символ если да): "
        #             )
        #         )
        #         role_id = int(input("ID роли: "))

        #         is_update = update_user_by_id(
        #             conn,
        #             user=User(
        #                 id=id,
        #                 nickname=nickname,
        #                 email=email,
        #                 steam_level=steam_level,
        #                 hours_played=hours_played,
        #                 last_online=last_online,
        #                 is_online=is_online,
        #                 role_id=role_id,
        #             ),
        #         )

        #         if is_update == True:
        #             print("успешно обновлено")
        #         else:
        #             print(f"пользователь c id {id} не найден")
        #     elif menu_number == 0:
        #         is_run = False

        #     input("\n\n\nдля продолжения нажмите <Enter>\n\n\n")
        except Exception as e:
            print(
                f"Ошибка в работе с программой. Кратко: {str(e)}. Подробно: {repr(e)}"
            )
