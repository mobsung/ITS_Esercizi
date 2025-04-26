'''
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Codice Driver
Aggiungi libri alla biblioteca.
Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
Mostra i libri disponibili in ogni fase.
Visualizza lo stato finale di ogni libro.
'''



class Libro():

    def __init__(self, titolo:str, autore:str):

        self.setTitle(titolo)
        self.setAutor(autore)
        self.stato_prestito = "disponibile" # Stato iniziale per l'attributo self.stato_prestito


    # Metodo che consente di impostare self.titolo
    def setTitle(self, title:str) -> None:

        self.titolo = title


    # Metodo che consente di impostare self.autore
    def setAutor(self, autor:str) -> None:

        self.autore = autor


    # Metodo che consente di impostare self.stato_prestito
    def setStatoPrestito(self, stato_prestito:str) -> None:

        self.stato_prestito = stato_prestito

    
    # Metodo che restituisce il valore di self.titolo
    def getTitle(self) -> str:

        return self.titolo
    

    # Metodo che restituisce il valore di self.autore
    def getAutor(self) -> str:

        return self.autore
    

    # Metodo che restituisce il valore di self.stato_prestito
    def getStatoPrestito(self) -> str:

        return self.stato_prestito
    
    
    # Metodo speciale per rendere uguali tutti gli oggetti che hanno lo stesso attributo self.titolo e self.autore
    def __eq__(self, other):

        if other is None or not isinstance(other, type(self)):
            return False
        
        else:
            return self.getTitle() == other.getTitle() and self.getAutor() == other.getAutor()


    # Medoto speciale che rende l'oggetto hashable usando titolo e autore come identificatori 
    def __hash__(self):

        return hash((self.titolo, self.autore))


if __name__ == "__main__":

    libro1: Libro = Libro("Libro bello", "Quello la")

    print(libro1)