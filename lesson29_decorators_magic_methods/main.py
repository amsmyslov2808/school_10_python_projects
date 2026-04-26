from cat import Cat

from my_math import MyMath

cat = Cat("Пушок", 1)
print(Cat.count)

cat2 = Cat("Пушок 2", 3)
print(Cat.count)

# print(cat.__dict__)

print(cat)
print(cat2)

print(cat.name)
cat.name = "X"
print(cat.name)

# print(cat.get_name())
# cat.set_name("X")
# print(cat.get_name())

# cat3 = Cat("Пушок 3", 5)

print(MyMath.mul(2, 4))
