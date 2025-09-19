'''
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    - init(id, title): metodo costruttore.

    - setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.

    - setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.

    - getID(): che consente di ritornare il valore del codice identificativo di un film.

    - getTitle(): che consente di ritornare il valore del titolo di un film.

    - isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
'''


from typing import Self

class Film:

    __id: int
    __title: str

    def __init__(self, id: int, title: str) -> None:
        self.setID(id)
        self.setTitle(title)

    def setID(self, id: int) -> None:
        if id and type(id) == int:
            self.__id = id

    def setTitle(self, title: str) -> None:
        if title and type(title) == str:
            self.__title = title

    def getID(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherFilm: Self) -> bool:
        return True if self.getID() == otherFilm.getID() else False


if __name__ == '__main__':

    f1: Film = Film(id=1, title='a')
    f2: Film = Film(id=1, title='a')

    print(f1.isEqual(f2))