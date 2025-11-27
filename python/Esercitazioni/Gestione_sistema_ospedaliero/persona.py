'''
Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
- La classe Persona deve avere i seguenti metodi:

    - init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.

    - setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".

    - setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

    - setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

    - getName(): consente di ritornare il nome di una persona.

    - getLastname(): consente di ritornare il cognome di una persona.

    - getAge(): consente di ritornare l'età di una persona.

    - greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
'''


class Persona:

    def __init__(self, first_name: str, last_name: str) -> None:

        self.setName(first_name)
        self.setLastName(last_name)

        if self.__first_name != None and self.__last_name != None:
            self.__eta = 0
        else:
            self.__eta = None

    def setName(self, first_name: str) -> None:

        if first_name and type(first_name) == str:
            self.__first_name = first_name
        else:
            self.__first_name = None
            print('Il nome inserito non è una stringa!')

    def setLastName(self, last_name: str) -> None:

        if last_name and type(last_name) == str:
            self.__last_name = last_name
        else:
            self.__last_name = None
            print('Il cognome inserito non è una stringa!')

    def setAge(self, eta: int) -> None:

        if eta and type(eta) == int and eta >= 0:
            self.__eta = eta
        else:
            print('L\'età deve essere un numero intero!')

    def getName(self) -> str:

        return self.__first_name

    def getLastname(self) -> str:

        return self.__last_name
    
    def getAge(self) -> int:

        return self.__eta
    
    def greet(self) -> None:

        return(f'Ciao, sono {self.getName()} {self.getLastname()}! Ho {self.getAge()} anni!')
    

if __name__ == '__main__':  

    p1: Persona = Persona(first_name=1, last_name='Rossi')

    p1.setAge('1')

    print(p1.getAge())
    print(p1.getName())
    print(p1.getLastname())

    p1.greet()

