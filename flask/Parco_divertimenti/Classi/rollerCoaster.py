'''
Classe RollerCoaster

La classe RollerCoaster rappresenta una montagna russa e eredita da Ride.

Attributi aggiuntivi:

    inversions: numero di inversioni presenti nel tracciato (ad esempio 3 o 5).

Metodi:

    category(): restituisce la stringa "roller_coaster".
    base_wait(): restituisce l’attesa base in minuti (ad esempio 40).
    info(): estende il metodo della superclasse includendo anche il numero di inversioni.
'''


from Classi.ride import Ride

class RollerCoaster(Ride):

    def __init__(self, ride_id: str, name: str, min_height: int, inversions: int = 4) -> None:
        super().__init__(ride_id, name, min_height)
        self.inversions = inversions

    def category(self) -> str:
        return 'roller_coaster'
    
    def base_wait(self) -> None:
        return 40
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict['inversions'] = self.inversions
        return info_dict
    
    def __repr__(self):
        return f'{self.name}'
    

if __name__ == '__main__':

    r = RollerCoaster('s', 'r1', 23)

    print(r.info())


