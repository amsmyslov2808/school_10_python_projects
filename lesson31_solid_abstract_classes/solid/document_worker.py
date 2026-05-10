from abc import ABC, abstractmethod


class DocumentWorker(ABC):
    @abstractmethod
    def save(
        self,
        text: str,
    ):
        pass

    @abstractmethod
    def load(self):
        pass
