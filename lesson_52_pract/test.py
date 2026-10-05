from dataclasses import dataclass

@dataclass
class Cat:
    name:str
    age:int

cat = Cat("barsik",3)
cat.name = "misha"
