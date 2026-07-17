from sqlalchemy import (
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

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/pdd_db"


class Base(DeclarativeBase):
    pass


class SignCategory(Base):
    __tablename__ = "sign_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)


class RoadSign(Base):
    __tablename__ = "road_signs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("sign_categories.id", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
    )

    category: Mapped[SignCategory] = relationship(back_populates="sign_categories")

    image_path: Mapped[str] = mapped_column(String(2000), nullable=False)


engine = create_engine(DATABASE_URL, echo=False)

get_session_local = sessionmaker(
    bind=engine,
    expire_on_commit=True,
)

with get_session_local() as session:
    is_run = True

    while is_run == True:
        try:
            road_signs = get_all_road_signs_with_category(session)
            print_all_road_signs_with_category(road_signs)

            print("\n" + "*" * 50 + "\n")

            sign_categories = get_all_sign_categories(session)
            print_sign_categories(roles)

            print("\n" + "=" * 100 + "\n")

            print("Меню:")
            print("1. Вывести знак по id")
            print("2. Добавить ноый знак")
            print("3. Удалить знак по id")
            print("4. Обновить знак по id")

            print("0. Выход")

            menu_number = int(input("выберите пункт меню: "))

            if menu_number == 1:
                id = int(input("введите id знака: "))

                road_sign = get_road_sign_by_id(session, id)

                print_road_signs_table_header()

                if road_sign == None:
                    print(f"знак с id {id} не найден")
                else:
                    print_one_road_sign(road_sign)
            elif menu_number == 2:
                name = input("название: ")
                description = input("описание: ")
                category_id = int(input("ИД категории знака: "))
                image_path = input("url изображения знака: ")

                add_new_road_sign(
                    session,
                    road_sign=RoadSign(
                        name=name,
                        description=description,
                        category_id=category_id,
                        image_path=image_path,
                    ),
                )

                print("успешно добавлено")
            elif menu_number == 3:
                id = int(input("введите id знака: "))

                is_deleted = delete_road_sign_by_id(session, id)

                if is_deleted == True:
                    print("успешно удалено")
                else:
                    print(f"знак с id {id} не найден")
            elif menu_number == 4:
                id = int(input("введите id знака: "))

                name = input("название: ")
                description = input("описание: ")
                category_id = int(input("ИД категории знака: "))
                image_path = input("url изображения знака: ")

                is_updated = update_user_by_id(
                    session,
                    road_sign=RoadSign(
                        id=id,
                        name=name,
                        description=description,
                        category_id=category_id,
                        image_path=image_path,
                    ),
                )

                if is_updated == True:
                    print("успешно обновлено")
                else:
                    print(f"знак с id {id} не найден")
            elif menu_number == 0:
                is_run = False

            input("\n\n\nдля продолжения нажмите <Enter>\n\n\n")
        except Exception as e:
            print(
                f"Ошибка в работе с программой. Кратко: {str(e)}. Подробно: {repr(e)}"
            )
            is_run = False
