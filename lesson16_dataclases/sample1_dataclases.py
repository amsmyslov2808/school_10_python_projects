from dataclasses import dataclass


@dataclass
class MobilePhone:
    id: int
    name: str
    price: int
    amount: int


# mobile1 = MobilePhone(1, "iPhone 17", 85000, 15)
# mobile2 = MobilePhone(2, "Xiaome 14", 50000, 18)

mobiles = []

mobiles.append(MobilePhone(1, "iPhone 17", 85000, 15))
mobiles.append(MobilePhone(2, "Xiaome 14", 50000, 18))

# for item in mobiles:

for i in range(len(mobiles)):
    print(
        f"id: {mobiles[i].id} model: {mobiles[i].name} price: {mobiles[i].price} amount: {mobiles[i].amount}"
    )
