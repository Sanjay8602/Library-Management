import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("123456789", "Test Book", "Author Sanjay", 2024)

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn("123456789", self.library.books)

    def test_borrow_book(self):
        self.library.add_book(self.book)
        self.library.borrow_book("123456789")
        self.assertFalse(self.library.books["123456789"].is_available)

    def test_borrow_unavailable_book(self):
        self.library.add_book(self.book)
        self.library.borrow_book("123456789")
        with self.assertRaises(ValueError):
            self.library.borrow_book("123456789")

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("987654321")
if __name__ == "__main__":
    unittest.main()