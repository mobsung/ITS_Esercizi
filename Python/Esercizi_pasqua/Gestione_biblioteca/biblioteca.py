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


from libro import Libro


class Biblioteca():

    def __init__(self):
        
        self.catalogo: dict[Libro, dict[str, str]] = {}
        self.libri_prestati: dict[str, int] = {}


    # Metodo che consente di aggiungere libri nella biblioteca
    def aggiungi_libro(self, libro :Libro) -> None:

        if libro not in self.catalogo: # Verifica se il libro è già presente nel catalogo
            self.catalogo[libro] = {"titolo": libro.getTitle(), "autore": libro.getAutor(), "stato_prestito": libro.getStatoPrestito(), "quandità": 1}
            self.libri_prestati[libro.getTitle()] = 0

        else:
            self.catalogo[libro]["quandità"] += 1 # Aggiunge 1 alla quantità se il libro è già presente nel catalogo

        print(f'--Aggiungi Libro--\nIl libro "{libro.getTitle()}" scritto da "{libro.getAutor()}" è stato aggiunto alla libreria!\n')


    # Metodo che restituisce una lista con tutti i libri prestati
    def mostra_libri_prestati(self) -> None:

        lista_libri_prestati: str = "--Lista libri prestati--\n"
        
        for libro, quant in self.libri_prestati.items():

            lista_libri_prestati += f'Libro: "{libro}" - Quantità: {quant}\n'

        print(lista_libri_prestati)


    # Metodo che cconsente di prestare libri 
    def presta_libro(self, titolo: str) -> None:

        for info in self.catalogo.values(): # Ciclo che itera il catalogo 

            # Verifica se il titolo è già presente nel catalogo e lo stato_prestito è "disponibile"
            if titolo == info["titolo"] and info["stato_prestito"] == "disponibile":
                if info["quandità"] > 0: # Verifica se la quantità è maggiore di 0 
                    info["quandità"] -= 1
                    self.libri_prestati[titolo] += 1

                    if info["quandità"] == 0: # Quando la quantità arriva a 0, imposta lo stato_prestito a "non disponibile"
                        info["stato_prestito"] = "non disponibile" 

                print(f'--Presta Libro--\nIl libro "{titolo}" scritto da "{info["autore"]}" è stato prestato!\n')
                return
    
        print(f'--Presta Libro--\nIl libro "{titolo}" non è disponiblile!\n')


    def restituisci_libro(self, titolo: str):

        for info in self.catalogo.values(): # Ciclo che itera il catalogo

            # Aumenta la quantità nel catalogo solo se il libro è presente nel dizionario dei libri prestati
            if titolo == info["titolo"] and self.libri_prestati[titolo] > 0:
                info["quandità"] += 1
                self.libri_prestati[titolo] -= 1

                if info["quandità"] > 0: # Imposta lo stato_prestito a "dispoonibile" se la quantità è maggiore di 0
                        info["stato_prestito"] = "disponibile"

                print(f'--Restituisci Libro--\nIl libro "{titolo}" scritto da "{info["autore"]}" è stato restituito!\n')
                return
            
            else: 
                try: # Si usa Try in quanto la verifica titolo nel dizionario dà errore se il titolo non è presente nel dizionario
                    if self.libri_prestati[titolo] == 0:
                        print(f'--Restituisci Libro--\nImpossibile restituire il libro "{titolo}" in quanto tutte le copie sono presenti nella Biblioteca!\n')
                        return
                        
                except: # Restituisce messaggio non disponibile se il titolo non è presente nel catalogo
                    print(f'--Restituisci Libro--\nIl libro "{titolo}" non è disponiblile nella Biblioteca!\n')
                    return
                    

    # Metodo che stampa una lista con tutti i libri pesenti nella biblioteca
    def mostra_libri_disponibili(self) -> None:

        catalogo_libri: str = "--Lista libri--\n"

        if len(self.catalogo) > 0: 
            for info in self.catalogo.values():
                
                catalogo_libri += f'Titolo: "{info["titolo"]}" - Autore: "{info["autore"]}" - Disponibilità: >> {info["stato_prestito"]} << - Quantità: {info["quandità"]}\n'

            print(catalogo_libri)

        

if __name__ == "__main__":

    # Creazione oggetti Libro
    libro1: Libro = Libro("Libro Bello", "Quello la")
    libro2: Libro = Libro("Libro Brutto", "Non lo so")
    libro3: Libro = Libro("Libro Bello", "Quello la")

    # Creazione oggetto Biblioteca
    biblioteca1 :Biblioteca = Biblioteca()

    # Aggiunta dei libri nella bliblioteca
    biblioteca1.aggiungi_libro(libro1)
    biblioteca1.aggiungi_libro(libro2)
    biblioteca1.aggiungi_libro(libro3)
    
    
    # Prova prestito libri
    biblioteca1.presta_libro("Libro Bello")
    biblioteca1.presta_libro("Libro Brutto")
    
    # Mostra lista libri
    biblioteca1.mostra_libri_disponibili()

    
    # Prova restituzione libri
    biblioteca1.restituisci_libro("Libro Bello")
    biblioteca1.restituisci_libro("Libro Brutto")

    # Mostra lista libri
    biblioteca1.mostra_libri_disponibili()


    # Prova prestito libri
    biblioteca1.presta_libro("Libro Bello")
    biblioteca1.presta_libro("Libro Brutto")
    
    # Mostra lista libri
    biblioteca1.mostra_libri_disponibili()


    # Prova con libro inesistente
    biblioteca1.restituisci_libro("Libro Inesistente")


    # Mostra libri non restituiti
    biblioteca1.mostra_libri_prestati()


