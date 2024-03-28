import pandas as pd
import unittest

class BookLover():
    name = ''
    email = ''
    fav_genre = ''
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        #self.num_books = num_books
        #self.book_rating = book_rating
                        
    #Method 1: 
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [book_rating]})
        if self.has_read(book_name):
            return False
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return True
       
    #Method 2:
    def has_read(self, book_name):
        return any(self.book_list.book_name == book_name)
    
    #Method 3:
    def num_books_read(self):
        #return the length of book_list (number)
        return(len(self.book_list))
    
    #Method 4:
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
