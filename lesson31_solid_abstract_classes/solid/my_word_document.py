from document_worker import DocumentWorker


class MyWordDocument:
    text: str
    font_size: int

    def __init__(self) -> None:
        self.text = "Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев настоящей рыбы, то есть текста, который визуально напоминает печатное издание"
        self.font_size = 12

    def print_info(self):
        print(f"вывести шрифтом: {self.font_size}\nтекст: {self.text}")

    def save(self, document_worker: DocumentWorker):
        document_worker.save(self.text)

    def load(self, document_worker: DocumentWorker):
        document_worker.load()
