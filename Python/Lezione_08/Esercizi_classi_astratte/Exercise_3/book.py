'''
Create a Book class containing the following attributes: title, author, isbn. The book class must contains the following methods:

__str__, method to return a string representation of the book.

from_string, a class method to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 
book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
In this case, divina_commedia should be an instance of the Book class with:

title = "La Divina Commedia"

author = "D. Alighieri"

isbn = "999000666"
'''

class Book:

    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f'Title: {self.title} - Author: {self.author} - ISBN: {self.isbn}'
    
    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(", ")
        return cls(title, author, isbn)
    
    def __eq__(self, other):

        if other is None or not isinstance(other, type(self)):
            return False
        
        else:
            return self.title == other.title and self.author == other.author and self.isbn == other.isbn

    def __hash__(self):

        return hash((self.title, self.author, self.isbn))
    

if __name__ == '__main__':

    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)
    
    print(divina_commedia)