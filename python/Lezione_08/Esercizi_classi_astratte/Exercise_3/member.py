'''
Create a Member class with the following attributes: name, member_id, borrowed_books. The member class must contain the following methods:

borrow_book, to add a book to the borrowed_books list.

return_book, to remove a book from the borrowed_books list.

__str__, method to return a string representation of the member.

from_string, a class method to create a Member instance from a string in the format "name, member_id". It means that you must use the class reference cls to create a new object of the Member class using a string.
'''

from book import Book

class Member:

    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books: list[Book] = []

    def __str__(self) -> str:
        borrowed_str = ', '.join(str(book) for book in self.borrowed_books)
        return f'Name: {self.name} - ID: {self.member_id} - Borrowed books: {borrowed_str}'
    
    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print(f'There is no book named {book} in the list')
        
    @classmethod
    def from_string(cls, member_str):
        name, member_id = member_str.split(", ")
        return cls(name, member_id)
    
    def __eq__(self, other):

        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.name == other.name and self.member_id == other.member_id

    def __hash__(self):

        return hash((self.name, self.member_id))
    

if __name__ == '__main__':

    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)
    book1: Book = Book('tile prova', 'quello la', 416548546)
    
    member_str: str = 'King, #1234'
    king: Member = Member.from_string(member_str)
    king.borrw_book(divina_commedia)
    king.borrw_book(book1)
    king.return_book(book1)
    king.return_book(book1)
    print(king)

