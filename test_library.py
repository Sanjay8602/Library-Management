import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("123456789", "Test Book", "Author Sanjay", 2024)

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn("123456789", self.library.books)

if __name__ == "__main__":
    unittest.main()