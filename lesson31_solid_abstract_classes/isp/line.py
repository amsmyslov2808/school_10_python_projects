from shape_line import ShapeLine
from shape import Shape


class Line(ShapeLine, Shape):
    x1: int
    x2: int
    y1: int
    y2: int

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw_line(self):
        print(f"вывод линии ({self.x1};{self.y1}) - ({self.x2};{self.y2})")

    def get_color(self) -> str:
        return "#FF00000"
