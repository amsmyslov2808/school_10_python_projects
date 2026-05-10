from abc import ABC, abstractmethod


class ShapeCirlce(ABC):
    @abstractmethod
    def draw_circle(self):
        pass
