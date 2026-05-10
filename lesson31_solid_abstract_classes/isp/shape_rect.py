from abc import ABC, abstractmethod


class ShapeRect(ABC):
    @abstractmethod
    def draw_rect(self):
        pass
