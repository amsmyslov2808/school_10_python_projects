# class Cat:
#     name: str
#     age: int

#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __eq__(self, value):
#         return self.name == value.name and self.age == value.age


# cat1 = Cat("Barsik", 1)
# cat2 = Cat("Barsik", 1)

# print(cat1 == cat2)
# print(cat1.__eq__(cat2))

# print(cat1)

# from dataclasses import dataclass


# @dataclass
# class Cat:
#     name: str
#     age: int

#     def meow(self):
#         print("meow")


# cat1 = Cat("Barsik", 1)
# cat2 = Cat("Barsik", 1)

# print(cat1 == cat2)

# print(cat1)

# cat1.meow()


class A:
    aa: int
    bb: str

    def __init__(self, aa: int, bb: str):
        self.aa = aa
        self.bb = bb
