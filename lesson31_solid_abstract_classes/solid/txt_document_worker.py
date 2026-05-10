from document_worker import DocumentWorker


class TxtDocumentWorker(DocumentWorker):
    file_name: str

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def save(
        self,
        text: str,
    ):
        print(f"документ с содержимым {text} сохранён в {self.file_name} файл")

    def load(self):
        print(f"документ загружен из {self.file_name} файла")
