'''
Classe astratta Volo:
Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di volo, come il codice del volo (stringa) e la capacità massima di posti disponibili sul volo (numero intero) che sono attributi passati come argomenti in input. Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili().
'''

from abc import ABC, abstractmethod


class Volo(ABC):

    codice_volo: str
    cap_massima: int
    prenotazioni: int

    def __init__(self, codice_volo: str, cap_massima: int) -> None:
        self.codice_volo = codice_volo
        self.cap_massima = cap_massima
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self) -> None:
        pass

    @abstractmethod
    def posti_disponibili(self) -> None:
        pass

    def codiceVolo(self) -> str:
        return self.codice_volo
    
    def capacitaMassima(self) -> None:
        return self.cap_massima
    
    def getPrenotazioni(self) -> int:
        return self.prenotazioni
    