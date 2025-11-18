'''
Classe Park

La classe Park rappresenta il contenitore principale del sistema, che gestisce tutte le attrazioni presenti nel parco.

Attributi:

    rides: dizionario che associa a ogni identificativo (id) l’oggetto Ride corrispondente.

Metodi:

    add(ride): aggiunge un’attrazione al parco.
    get(ride_id): restituisce l’attrazione corrispondente all’ID specificato oppure None se non esiste.
    list_all(): restituisce una lista di tutte le attrazioni (puoi ordinare per categoria e nome, opzionale).

Nel codice principale dovrà essere creato un parco e dovranno essere create almeno due attrazioni, una di tipo RollerCoaster e una di tipo Carousel.
'''


from Classi.carousel import Carousel
from Classi.rollerCoaster import RollerCoaster

class Park:

    def __init__(self) -> None:
        self.rides: dict[str, Carousel | RollerCoaster] = {}

    def add(self, ride: Carousel | RollerCoaster) -> None:
        if ride:
            self.rides[ride.ride_id] = ride

    def get(self, ride_id: str) -> Carousel | RollerCoaster | None:
        if ride_id in self.rides:
            return self.rides[ride_id]
        else:
            return None
        
    def list_all(self) -> list[RollerCoaster | Carousel]:
        all_list: list[RollerCoaster | Carousel] = [self.rides[ride] for ride in self.rides]
        return all_list
    

if __name__ == '__main__':

    par1 = Park()

    cau1 = Carousel(ride_id='#1', name='Caurusel1', min_height=100)
    cau2 = Carousel(ride_id='#3', name='Caurusel2', min_height=120)
    roll1 = RollerCoaster(ride_id='#2', name='RollerCoaster1', min_height=140)
    roll2 = RollerCoaster(ride_id='#4', name='RollerCoaster2', min_height=180)

    par1.add(cau1)
    par1.add(cau2)
    par1.add(roll1)
    par1.add(roll2)

    print(cau1.info())
    print(cau2.info())
    print(roll1.info())
    print(roll2.info())

    print(par1.list_all())