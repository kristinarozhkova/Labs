class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("Book already borrowed")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book was not borrowed")
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        return [book for book in self.books if not book.is_borrowed]
