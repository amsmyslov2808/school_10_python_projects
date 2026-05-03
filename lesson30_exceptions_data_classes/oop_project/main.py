from data_layer.books_storage import BookStorage
from service_layer.books_service import BooksService
from ui_layer.console_ui import ConsoleUI

books_storage = BookStorage()
books_service = BooksService(books_storage)
console_ui = ConsoleUI(books_service)

console_ui.start()
