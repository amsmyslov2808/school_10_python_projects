from infastructure_layer.exceptions import *


class ConsoleUI:
    def __init__(self, books_service):
        self.books_service = books_service

    def start(self):
        while True:
            print()
            print("=== КОНСОЛЬНАЯ БИБЛИОТЕКА ===")
            print("1. Добавить книгу")
            print("2. Показать все книги")
            print("3. Отметить книгу как прочитанную")
            print("0. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.show_books()

            elif choice == "3":
                self.mark_book_as_read()

            elif choice == "0":
                print("Программа завершена")
                break

            else:
                print("Нет такой команды")

    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")

        try:
            self.books_service.add_book(title, author)
            print("Книга успешно добавлена")

        except LibraryError as error:
            print(f"Ошибка: {error}")

    def show_books(self):
        books = self.books_service.get_books()

        if len(books) == 0:
            print("Библиотека пустая")
            return

        print("Список книг:")

        for book in books:
            print(book)

    def mark_book_as_read(self):
        title = input("Введите название книги: ")

        try:
            self.books_service.mark_book_as_read(title)
            print("Книга отмечена как прочитанная")

        except LibraryError as error:
            print(f"Ошибка: {error}")
