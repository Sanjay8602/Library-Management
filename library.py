class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book already exists in the library.")
        self.books[book.isbn] = book