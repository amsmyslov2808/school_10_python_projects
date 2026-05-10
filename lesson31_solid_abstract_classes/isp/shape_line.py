from abc import ABC, abstractmethod


class ShapeLine(ABC):
    @abstractmethod
    def draw_line(self):
        pass
