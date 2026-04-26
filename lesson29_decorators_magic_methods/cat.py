from animal import Animal


class Cat(Animal):
    __name: str
    __age: int

    count: int = 0
    MAX_COUNT: int = 2

    def __init__(self, name: str, age: int):

        if Cat.count < Cat.MAX_COUNT:
            self.__name = name
            self.__age = age

            Cat.count += 1
        else:
            raise Exception("Ошибка. Вы создали слишком много котов")

    def make_sound(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Кот, Имя: {self.__name} Возраст: {self.__age}"

    @property
    def name(self):
        return self.__name + "!!!"

    @name.setter
    def name(self, value: str):
        if len(value) < 1 or len(value) > 30:
            raise Exception("Ошибка. Слишком короткое или длинное имя")

        self.__name = value

    # def get_name(self):
    #     return self.__name

    # def set_name(self, name: str):
    #     if len(name) < 1 or len(name) > 30:
    #         raise Exception("Ошибка. Слишком короткое или длинное имя")

    #     self.__name = name
