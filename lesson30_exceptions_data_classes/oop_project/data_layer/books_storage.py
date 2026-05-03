class BookStorage:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def get_all(self):
        return self.books

    def find_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None
