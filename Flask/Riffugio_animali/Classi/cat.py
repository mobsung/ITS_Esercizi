'''
Classe Cat

La classe Cat rappresenta un gatto e eredita da Animal.
Attributi aggiuntivi

    indoor_only: booleano che indica se il gatto vive solo in casa (True/False),

    favorite_toy: stringa che rappresenta il gioco preferito (es. "ball", "mouse").

Metodi

    species(): restituisce la stringa "cat".

    daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
    Anche qui puoi usare una formula plausibile, ad esempio:
     
    return 100 + age_years * 30

    info(): estende il metodo della superclasse includendo anche indoor_only e favorite_toy.

'''

from Classi.animal import Animal

class Cat(Animal):

    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, favourite_toy: str, indoor_only: bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.favourite_toy = favourite_toy
        self.indoor_only = indoor_only

    def species(self) -> str:
        return 'cat'
    
    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict['favourite_toy'] = self.favourite_toy
        info_dict['indoor_only'] = self.indoor_only

        return info_dict