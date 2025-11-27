'''
La classe Ride rappresenta un’attrazione generica del parco. È una classe astratta e non può essere istanziata direttamente.
Ogni attrazione ha:

    un identificativo (id) di tipo stringa;
    un nome (name) di tipo stringa;
    un’altezza minima richiesta (min_height_cm) di tipo intero.

Metodi:

    category(): metodo astratto. Deve essere implementato nelle sottoclassi per restituire la categoria dell’attrazione (es. "roller_coaster", "family").
    base_wait(): metodo astratto. Deve essere implementato nelle sottoclassi e deve restituire l’attesa base in minuti.
    info(): metodo concreto che restituisce un dizionario con le informazioni principali dell’attrazione (id, nome, altezza minima, categoria e attributi specifici).
    wait_time(crowd_factor: float = 1.0): metodo concreto che restituisce l’attesa stimata in minuti. L’attesa è calcolata come base_wait() * crowd_factor, arrotondata all’intero positivo.
'''


from abc import ABC, abstractmethod
from typing import Any

class Ride:

    def __init__(self, ride_id: str, name: str, min_height: int) -> None:
        self.ride_id = ride_id
        self.name = name
        self.min_height = min_height

    @abstractmethod
    def category(self) -> None:
        pass

    @abstractmethod
    def base_wait(self) -> None:
        pass

    def info(self) -> dict:
        info_dict: dict[str, Any] = {
            'ride_id': self.ride_id,
            'name': self.name,
            'min_height': self.min_height,
            'category': self.category()
        }
        return info_dict

    def crowd_factor(self, crowd_factor: float = 1.0) -> int:
        return round(self.base_wait() * crowd_factor)



