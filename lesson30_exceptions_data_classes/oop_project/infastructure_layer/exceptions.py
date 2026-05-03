class LibraryError(Exception):
    pass


class EmptyTitleError(LibraryError):
    pass


class EmptyAuthorError(LibraryError):
    pass


class BookAlreadyExistsError(LibraryError):
    pass


class BookNotFoundError(LibraryError):
    pass
