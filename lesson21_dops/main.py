from Cat import Cat

from Cat_Shelter import CatShelter

cat_shelter = CatShelter("Мурзилка", "ул. Пушкинская, 10", "+7 (123) 456-78-90")

cat_shelter.add_cat(Cat("Барсик", 3, True))
cat_shelter.add_cat(Cat("Мурка", 5, False))
cat_shelter.add_cat(Cat("Васька", 2, True))
cat_shelter.add_cat(Cat("Пушок", 4, False))

cat_shelter.print_info()


# c1 = Cat("Барсик", 3, True)

# print(c1.get_name())
# print(c1.get_age())
# print(c1.get_is_happy())

# print(c1.get_info())

# c1.set_is_happy(False)
# c1.set_is_happy(True)

# c1.make_happy()
# c1.make_unhappy()
