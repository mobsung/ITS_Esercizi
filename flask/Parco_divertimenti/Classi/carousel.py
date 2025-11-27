'''
Classe Carousel

La classe Carousel rappresenta una giostra con animali e eredita da Ride.

Attributi aggiuntivi:

    animals: lista di animali presenti sulla giostra (ad esempio ["horse", "swan", "tiger"]).

Metodi:

    category(): restituisce la stringa "family".
    base_wait(): restituisce l’attesa base in minuti (ad esempio 10).
    info(): estende il metodo della superclasse includendo la lista di animali.
'''

from Classi.ride import Ride

class Carousel(Ride):

    def __init__(self, ride_id: str, name: str, min_height: int, animals = ["horse", "swan", "tiger"]) -> None:
        super().__init__(ride_id, name, min_height)
        self.animals = animals

    def category(self) -> str:
        return 'family'
    
    def base_wait(self) -> int:
        return 10
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict['animals'] = self.animals
        return info_dict
    
    def __repr__(self):
        return f'{self.name}'

    