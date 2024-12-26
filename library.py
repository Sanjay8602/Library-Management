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
        
    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found in the library.")
        if not self.books[isbn].is_available:
            raise ValueError("Book is currently unavailable.")
        self.books[isbn].is_available = False
        
    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found in the library.")
        if self.books[isbn].is_available:
            raise ValueError("Book was not borrowed.")
        self.books[isbn].is_available = True
        
    def view_available_books(self):
        return [book for book in self.books.values() if book.is_available]