'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

'''
class Book:
    
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self) -> None:
        if self.is_borrowed:
            print(f"Il libro '{self.title}' è già noleggiato.")
        else:
            self.is_borrowed = True

    def return_book(self) -> None:
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            print(f"Il libro '{self.title}' non è stato noleggiato da questo cliente.")

    '''
    Attributi:
        book_id: str - Identificatore di un libro.
        title: str - titolo del libro.
        author: str - autore del libro
        is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
    Metodi:
        borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
        return_book()- Contrassegna il libro come restituito.
    '''

class Member:
    
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        if book.is_borrowed:
            print(f"Il libro '{book.title}' è già noleggiato.")
        else:
            book.borrow()
            self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Il libro '{book.title}' non è stato noleggiato da questo cliente.")

    '''
    Attributi:
        member_id: str - identificativo del membro.
        name: str - il nome del membro.
        borrowed_books: list[Book] - lista dei libri presi in prestito.
    Metodi:
        borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
        return_book(book): rimuove il libro dalla lista borrowed_books.
    '''


class Library:

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str) -> None:
        if not self.books.get(book_id):
            self.books[book_id] = Book(book_id=book_id, title=title, author=author)
        else:
            print(f"Il film con ID '{book_id}' esiste già.")

    def register_member(self, member_id: str, name: str) -> None:
        if not self.members.get(member_id):
            self.members[member_id] = Member(member_id=member_id, name=name)
        else:
            print(f"Il cliente con ID '{member_id}' è già registrato.")

    def borrow_book(self, member_id: str, book_id: str) -> None:
        if self.members.get(member_id) and self.books.get(book_id):
            self.members[member_id].borrow_book(self.books[book_id])
        else:
            print("Cliente o film non trovato.")
    
    def return_book(self, member_id: str, book_id: str) -> None:
        if self.members.get(member_id) and self.books.get(book_id):
            self.members[member_id].return_book(self.books[book_id])
        else:
            print("Cliente o film non trovato.")

    def get_borrowed_books(self, member_id: str) -> list[Book]:
        if self.members.get(member_id):
            return self.members.get(member_id).borrowed_books
        else:
            print("Cliente non trovato.")
            return []
        
    
    '''
    Attributi:
        books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
        members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
    Metodi:
        add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
        register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
        borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
        return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
        get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

    '''