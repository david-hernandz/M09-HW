
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        test_name = "Test Book"
        test_rating = 10
        book_lover.add_book(test_name, test_rating)
        self.assertTrue(book_lover.has_read(test_name))
                               
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        test_name = "Test Book"
        test_rating = 10
        book_lover.add_book(test_name, test_rating)
        book_lover.add_book(test_name, test_rating)
        expected = 1
        actual = len(book_lover.book_list[book_lover.book_list.book_name == test_name])
        self.assertEqual(expected, actual)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        test_name = "Test Book"
        test_rating = 10
        book_lover.add_book(test_name, test_rating)
        result = book_lover.has_read("Test Book")
        self.assertTrue(result)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        test_name = "Test Book"
        test_rating = 10
        book_lover.add_book(test_name, test_rating)
        result = book_lover.has_read("Another Book")
        self.assertFalse(result)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        book_lover.add_book("Book One", 8)
        book_lover.add_book("Book Two", 7)
        book_lover.add_book("Book Three", 10)
        expected_number_of_books = 3
        actual_number_of_books = book_lover.num_books_read()
        self.assertEqual(expected_number_of_books, actual_number_of_books)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_lover = BookLover("David H.", "fxj5fe@virginia.edu", "drama")
        book_lover.add_book("Book One", 8)
        book_lover.add_book("Book Two", 7)
        book_lover.add_book("Book Three", 10)
        book_lover.add_book("Book Four", 2)
        book_lover.add_book("Book Five", 1)
        #expected_books = ["Book One", "Book Two", "Book Three"]
        actual_books = book_lover.fav_books()
        #actual_book_names = [book for book, rating in actual_books if rating > 3]
        #expected_books.sort()
        #actual_book_names.sort()
        #self.assertEqual(expected_books, actual_book_names)
        self.assertTrue((actual_books.book_rating > 3).all(), "Failed: Some books have rating <= 3")
       
                
if __name__ == '__main__':

    unittest.main(verbosity=3)
