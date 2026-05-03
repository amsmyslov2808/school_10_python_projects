from data_layer.book import Book
from infastructure_layer.exceptions import *


class BooksService:
    def __init__(self, books_storage):
        self.books_storage = books_storage

    def add_book(self, title, author):
        title = title.strip()
        author = author.strip()

        if title == "":
            raise EmptyTitleError("Название книги не может быть пустым")

        if author == "":
            raise EmptyAuthorError("Автор книги не может быть пустым")

        existing_book = self.books_storage.find_by_title(title)

        if existing_book is not None:
            raise BookAlreadyExistsError("Такая книга уже есть в библиотеке")

        book = Book(title, author)
        self.books_storage.add(book)

    def get_books(self):
        return self.books_storage.get_all()

    def mark_book_as_read(self, title):
        title = title.strip()

        if title == "":
            raise EmptyTitleError("Название книги не может быть пустым")

        book = self.books_storage.find_by_title(title)

        if book is None:
            raise BookNotFoundError("Книга не найдена")

        book.mark_as_read()
