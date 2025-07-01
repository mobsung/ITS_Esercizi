'''
Classe astratta Volo:
Tale classe sarà utilizzata per definire nel suo costruttore le funzionalità base di ogni tipo di volo, come il codice del volo (stringa) e la capacità massima di posti disponibili sul volo (numero intero) che sono attributi passati come argomenti in input. Inoltre, la classe deve avere un attributo chiamato prenotazioni, il quale non deve essere passato come argomento del costruttore; il costruttore, però, deve assegnare valore iniziale pari a 0 a tale attributo.
 
Metodi:

    si definisca il metodo astratto prenota_posto().
    si definisca il metodo astratto posti_disponibili().
'''

from abc import ABC, abstractmethod


class Volo(ABC):

    _codice_volo: str
    _cap_massima: int
    _prenotazioni: int

    def __init__(self, codice_volo: str, cap_massima: int) -> None:
        self._set_codice_volo(codice_volo)
        self._set_cap_massima(cap_massima)
        self._prenotazioni = 0

    @abstractmethod
    def prenota_posto(self) -> None:
        pass

    @abstractmethod
    def posti_disponibili(self) -> int:
        pass

    def _set_codice_volo(self, codice_volo: str) -> None:
        self._codice_volo = codice_volo

    def _set_cap_massima(self, cap_massima: int) -> None:
        self._cap_massima = cap_massima

    # def codice_volo(self) -> str:
    #     return self._codice_volo
    
    # def capacita_massima(self) -> None:
    #     return self._cap_massima
    
    # def prenotazioni(self) -> int:
    #     return self._prenotazioni
    