'''
Create a Library class with the following attributes: books, members, total_books (i.e., a class attribute to keep track of the total number of Book instances). The library class must contain the following methods:

add_book, to add a book to the library and increment total_books.

remove_book, to remove a book from the library and decrement total_books.

register_member, to add a member to the library.

lend_book, to lend a book to a member. It should check if the book is available and if the member is registered.

__str__, method to return a string representation of the library with the list of books and members.

library_statistics,  a class method to print the total number of books.
'''

from member import Member
from book import Book

class Library:

    total_books: int = 0

    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
            Library.total_books += 1
        else:
            print('--> Il libro esiste già')

    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)
            Library.total_books -= 1
        else:
            print('--> Non esiste il libro nella libreria')

    def register_member(self, member: Member) -> None:
        if member not in self.members:
            self.members.append(member)
        else:
            print(f'--> Il membro con ID {member.member_id} è già stato registrato')

    def lend_book(self, book: Book, member: Member) -> None:
        if member in self.members and book in self.books:
            member.borrow_book(book)
            self.books.remove(book)
        else: 
            if member not in self.members:
                print(f'--> Il membro con ID {member.member_id} è già stato registrato')
            else:
                print(f'--> Il libro {book.title} non è presente nella libreria')

    def __str__(self):
        members_str = '\n'.join(str(member) for member in self.members)
        books_str = '\n'.join(str(book) for book in self.books)
        return f'-->Membri registrati:\n{members_str}\n-->Librbooks_stri disponibili:\n{books_str}'
    
    @classmethod
    def library_statistics(cls):
        print(f'Totale libri registrati: {cls.total_books}')

if __name__ == '__main__':

#-------------------------------------------------------------------------------------------------

    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)

    book_str1: str = "Il Nome della Rosa, U. Eco, 123456789"
    nome_della_rosa: Book = Book.from_string(book_str1)

    book_str2: str = "I Promessi Sposi, A. Manzoni, 987654321"
    promessi_sposi: Book = Book.from_string(book_str2)

    book_str3: str = "Cent'anni di Solitudine, G. García Márquez, 456123789"
    cent_anni_solitudine: Book = Book.from_string(book_str3)

    book_str4: str = "Il Gattopardo, G. Tomasi di Lampedusa, 321789654"
    gattopardo: Book = Book.from_string(book_str4)

    book_str5: str = "Se questo è un uomo, P. Levi, 741852963"
    se_questo_e_un_uomo: Book = Book.from_string(book_str5)

    book_list: list[Book] = [divina_commedia, nome_della_rosa, promessi_sposi, cent_anni_solitudine, gattopardo, se_questo_e_un_uomo]
#-------------------------------------------------------------------------------------------------    

    member_str1: str = "Mario Rossi, 1001"
    mario_rossi: Member = Member.from_string(member_str1)

    member_str2: str = "Lucia Bianchi, 1002"
    lucia_bianchi: Member = Member.from_string(member_str2)

    member_str3: str = "Giovanni Verdi, 1003"
    giovanni_verdi: Member = Member.from_string(member_str3)

    member_str4: str = "Anna Neri, 1004"
    anna_neri: Member = Member.from_string(member_str4)

    member_str5: str = "Paolo Gialli, 1005"
    paolo_gialli: Member = Member.from_string(member_str5)

    member_list: list[Member] = [mario_rossi, lucia_bianchi, giovanni_verdi, anna_neri, paolo_gialli]
#-------------------------------------------------------------------------------------------------

    library1: Library = Library()

    for book in book_list:
        library1.add_book(book)

    for member in member_list:
        library1.register_member(member)

    library1.lend_book(promessi_sposi, mario_rossi)

    print(library1)
    library1.library_statistics()