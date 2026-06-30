import psycopg
from psycopg.rows import class_row

from dataclasses import dataclass

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "online_food_store",
    "user": "postgres",
    "password": "12345",
}


@dataclass(slots=True)
class Order:
    id: int
    customer_name: str
    product_id: int
    quantity: int


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def get_orders(conn) -> list[Order]:
    with conn.cursor(row_factory=class_row(Order)) as cur:

        cur.execute("""SELECT 
                    id,
                    customer_name,
                    product_id,
                    quantity
                    FROM orders ORDER BY id ASC""")

        return list(cur.fetchall())


def get_total_quantity(orders: list[Order]):
    # total_quantity = 0

    # for order in orders:
    #     total_quantity += order.quantity

    # return total_quantity

    return sum(order.quantity for order in orders)


def print_orders(orders: list[Order]):

    print("Заказы:")

    print(f"{'id':<5}{'customer_name':<20}{'product_id':<12}{'quantity':<10}")

    for order in orders:
        print(
            f"{order.id:<5}"
            f"{order.customer_name:<20}"
            f"{order.product_id:<12}"
            f"{order.quantity:<10}"
        )


with get_connection() as conn:

    orders = get_orders(conn)

    print_orders(orders)

    # print(get_total_quantity(orders))
