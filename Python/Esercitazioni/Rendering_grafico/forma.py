'''
Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.
'''

from abc import ABC, abstractmethod

class Forma(ABC):

    name: str

    @abstractmethod
    def __init__(self):
        
        self.name = ''

    @abstractmethod
    def getArea(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
