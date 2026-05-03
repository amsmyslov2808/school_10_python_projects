class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def __str__(self):
        status = "прочитана" if self.is_read else "не прочитана"
        return f"{self.title} — {self.author} ({status})"
