class AbstractBrush:
    _sign: str
    _name: str

    def __init__(self, sign: str, name: str) -> None:
        self._sign = sign
        self._name = name

    def draw(self) -> None:
        raise NotImplementedError("не реализован метод draw")


class StarBrush(AbstractBrush):

    def __init__(self) -> None:
        super().__init__("*", "Звёздная кисть")

    def draw(self) -> None:
        print(self._name)
        print(self._sign)
        print(self._sign * 2)
        print(self._sign * 3)
        print(self._sign * 2)
        print(self._sign)


class DashBrush(AbstractBrush):

    def __init__(self) -> None:
        super().__init__(".", "Пунктирная кисть")

    def draw(self) -> None:
        print(self._name)
        print(self._sign * 20)


class Pen:
    __brush: AbstractBrush
    __thickness: int
    __color: str

    def __init__(self, brush: AbstractBrush, thickness: int, color: str) -> None:
        self.__brush = brush
        self.__thickness = thickness
        self.__color = color

    def set_new_brush(self, brush: AbstractBrush) -> None:
        self.__brush = brush

    def draw(self) -> None:
        print(f"Толщина: {self.__thickness}")
        print(f"Цвет: {self.__color}")
        self.__brush.draw()


pen: Pen = Pen(StarBrush(), 3, "Yellow")
pen.draw()

pen.set_new_brush(DashBrush())
pen.draw()

pen.set_new_brush(StarBrush())
pen.draw()
