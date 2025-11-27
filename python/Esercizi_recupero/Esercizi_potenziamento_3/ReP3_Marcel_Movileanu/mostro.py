'''
Mostro ( che eredita da Creatura) con le seguenti proprietà:
- attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. Inoltre, deve inizializzare assalto.

    il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con una lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.

    i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di vittoria e sconfitta siano valori validi. In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".

    ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA, ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.
'''

from creatura import Creatura
from random import randint

class Mostro(Creatura):

    _urlo_vittoria: str
    _gemito_sconfitta: str
    _assalto: list[int]

    def __init__(self, nome: str, urlo: str, gemito: str) -> None:
        super().__init__(nome)
        self._setVittoria(urlo)
        self._setSconfitta(gemito)
        self._setAssalto()

    def _setVittoria(self, urlo: str) -> None:
        if urlo:
            self._urlo_vittoria = urlo
        else:
            self._urlo_vittoria = 'GRAAAHHH'

    def _setSconfitta(self, gemito: str) -> None:
        if gemito:
            self._gemito_sconfitta = gemito
        else:
            self._gemito_sconfitta = 'Uuurghhh'

    def _setAssalto(self) -> None:
        self._assalto = []
        while len(self._assalto) <= 15:
            n: int = randint(1, 100)
            self._assalto.append(n) if n not in self._assalto else None

    def urlo_vittoria(self) -> str:
        return self._urlo_vittoria
    
    def gemito_scofitta(self) -> str:
        return self._gemito_sconfitta
    
    def assalto(self) -> list[int]:
        return self._assalto

    def __str__(self) -> str:
        return f"{''.join([char.lower() if index % 2 == 0 else char.upper() for index, char in enumerate(self.nome())])}"
        



if __name__ == '__main__':
    
    mos1: Mostro = Mostro(nome='godzilla', urlo='Wazaa!', gemito='Nooooo!')

    print(mos1)