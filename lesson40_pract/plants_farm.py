import psycopg
from psycopg.rows import dict_row, class_row

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "plants_farm",
    "user": "postgres",
    "password": "12345",
}


def get_connection():
    return psycopg.connect(**DB_CONFIG)


@dataclass(slots=True)
class Plant:
    plant_name: str
    planting_date: date
    height_cm: Decimal
    species_id: int
    id: int | None = None

    def planting_date_to_str(self):
        return self.planting_date.strftime("%d.%m.%Y")


def get_all_plants(conn):
    with conn.cursor(row_factory=class_row(Plant)) as cur:
        cur.execute("""
            SELECT
            id,
            plant_name,
            planting_date,
            height_cm,
            species_id
            FROM
            plants
            """)

        return list(cur.fetchall())


def get_plant_by_id(conn, id: int):
    with conn.cursor(row_factory=class_row(Plant)) as cur:
        cur.execute(
            """
            SELECT
            id,
            plant_name,
            planting_date,
            height_cm,
            species_id
            FROM
            plants
            WHERE id=%s
            """,
            (id,),
        )

        return cur.fetchone()


def add_new_plant(conn, plant: Plant):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO plants
            (plant_name, planting_date, height_cm, species_id)
            VALUES (%s, %s, %s, %s)
            """,
            (plant.plant_name, plant.planting_date, plant.height_cm, plant.species_id),
        )

    conn.commit()


def update_plant_by_id(conn, plant: Plant) -> bool:
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE plants
	        SET
            plant_name=%s,
            planting_date=%s,
            height_cm=%s,
            species_id=%s
	        WHERE id=%s
            """,
            (
                plant.plant_name,
                plant.planting_date,
                plant.height_cm,
                plant.species_id,
                plant.id,
            ),
        )

        updated_rows = cur.rowcount

    conn.commit()

    return updated_rows != 0


def delete_plant_by_id(conn, id: int) -> bool:
    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM plants
	        WHERE id=%s
            """,
            (id,),
        )

        deleted_rows = cur.rowcount

    conn.commit()

    return deleted_rows != 0


def get_input_plant() -> Plant:
    print("\n--- Ввод данных нового растения ---")

    name = input("Введите название растения: ").strip()

    # Строка конвертируется напрямую в дату
    planting_date = datetime.strptime(
        input("Введите дату посадки (ГГГГ-ММ-ДД): "), "%Y-%m-%d"
    ).date()

    # Строка конвертируется напрямую в Decimal
    height_cm = Decimal(input("Введите высоту в см: "))

    # Строка конвертируется напрямую в int
    species_id = int(input("Введите ID вида (species_id): "))

    return Plant(
        plant_name=name,
        planting_date=planting_date,
        height_cm=height_cm,
        species_id=species_id,
    )


def get_input_plant_with_id() -> Plant:
    print("\n--- Ввод данных нового растения ---")

    id = int(input("Введите id растения: "))

    name = input("Введите название растения: ").strip()

    # Строка конвертируется напрямую в дату
    planting_date = datetime.strptime(
        input("Введите дату посадки (ГГГГ-ММ-ДД): "), "%Y-%m-%d"
    ).date()

    # Строка конвертируется напрямую в Decimal
    height_cm = Decimal(input("Введите высоту в см: "))

    # Строка конвертируется напрямую в int
    species_id = int(input("Введите ID вида (species_id): "))

    return Plant(
        plant_name=name,
        planting_date=planting_date,
        height_cm=height_cm,
        species_id=species_id,
        id=id,
    )


def get_input_plant_id() -> int:
    return int(input("Введите id растения: "))


with get_connection() as conn:
    # plants = get_all_plants(conn)
    # print(plants)

    # plant = get_plant_by_id(conn, 1)
    # print(plant)

    # new_plant = get_input_plant()
    # add_new_plant(conn, new_plant)

    # plants = get_all_plants(conn)
    # print(plants)

    # update_plant = get_input_plant_with_id()
    # update_plant_by_id(conn, update_plant)

    # plants = get_all_plants(conn)
    # print(plants)

    delete_id = get_input_plant_id()
    delete_plant_by_id(conn, delete_id)

    plants = get_all_plants(conn)
    print(plants)
