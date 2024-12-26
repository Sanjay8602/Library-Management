import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("123456789", "Test Book", "Author Sanjay", 2024)

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn("123456789", self.library.books)

#test for adding/borrowing the books    
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
            
    
#test for returning the books    
    def test_return_book(self):
        self.library.add_book(self.book)
        self.library.borrow_book("123456789")
        self.library.return_book("123456789")
        self.assertTrue(self.library.books["123456789"].is_available)

    def test_return_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.return_book("987654321")

    def test_return_unborrowed_book(self):
        self.library.add_book(self.book)
        with self.assertRaises(ValueError):
            self.library.return_book("123456789")

#test for viewing the available books in the library
def test_view_available_books(self):
    self.library.add_book(self.book)
    book2 = Book("987654321", "Data Structures", "Author B", 2021)
    self.library.add_book(book2)
    self.library.borrow_book("123456789")
    available_books = self.library.view_available_books()
    self.assertEqual(len(available_books), 1)
    self.assertEqual(available_books[0].isbn, "987654321")

if __name__ == "__main__":
    unittest.main()