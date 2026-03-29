from decimal import Decimal
from foot_courier import FootCourier

foot_courier_1: FootCourier = None  # type: ignore

try:
    foot_courier_1 = FootCourier(
        name="John Doe",
        experience=5,
        rating=4.5,
        completed_orders=100,
        balance=Decimal("1500.00"),
        is_busy=True,
        max_distance=10.0,
        speed=5.0,
    )
except ValueError as e:
    print(f"Error creating FootCourier: {e}")
    exit(1)

foot_courier_1.print_info()

try:
    foot_courier_1.deliver_order(distance=15.0)
except ValueError as e:
    print(f"Error delivering order: {e}")

foot_courier_1.finish_shift()
foot_courier_1.print_info()
