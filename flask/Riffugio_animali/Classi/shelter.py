'''
Classe Shelter

La classe Shelter rappresenta il contenitore principale del sistema, che gestisce tutti gli animali presenti nel rifugio.
Attributi

    animals: dizionario che associa a ogni identificativo (id) l’oggetto Animal corrispondente, ad esempio:
     
    { "d1": <Dog ...>, "c1": <Cat ...>, ... }

    adoptions (opzionale ma consigliato): struttura dati per gestire lo stato di adozione, ad esempio un dizionario:
     
    { "d1": "Mario Rossi", "c1": "Luca Bianchi" }

    dove la chiave è l’id dell’animale e il valore è il nome dell’adottante.

Metodi

    add(animal): aggiunge un animale al rifugio.
    Se esiste già un animale con lo stesso id, puoi decidere se sovrascriverlo o ignorare l’operazione (nel contesto dell’esercizio è sufficiente una scelta semplice e documentata nei commenti).

    get(animal_id): restituisce l’oggetto Animal corrispondente all’ID specificato oppure None se non esiste.

    list_all(): restituisce una lista di tutte le istanze di Animal presenti nel rifugio (puoi decidere se restituire direttamente gli oggetti o piuttosto una lista di dizionari generati con info()).

    is_adopted(animal_id): restituisce True/False a seconda che l’animale risulti adottato nella struttura adoptions.

    set_adopted(animal_id, adopter_name): registra l’adozione per un dato animale, salvando il nome dell’adottante.

Nel codice principale dovrà essere creato un rifugio e dovranno essere creati almeno due animali, uno di tipo Dog e uno di tipo Cat, che saranno aggiunti al rifugio prima di avviare l’app Flask.
'''

from random import randint

from Classi.cat import Cat
from Classi.dog import Dog


class Shelter:

    def __init__(self) -> None:
        self.animals: dict[str, Cat | Dog] = {}
        self.adoptions: dict[str, str] = {}

    def add_animal(self, animal: Cat | Dog) -> None:
        if animal and animal.id not in self.animals:
            self.animals[animal.id] = animal
        

        # se l'id esiste già si genera un nuovo id e si assegna all'animale
        else:
            new_id = f'{hash((randint(1, 10000), len(self.animals)))}'
            animal.set_id(new_id)
            self.animals[animal.id] = animal


    def get(self, animal_id: str) -> Cat | Dog | None:
        return self.animals.get(animal_id)
    

    def list_all(self) -> list[Cat, Dog]:
        all_list: list[Cat | Dog] = [self.animals[animal] for animal in self.animals]

        return all_list
    
    def is_adopted(self, animal_id: str) -> bool:
        return True if animal_id in self.adoptions else False
    
    def set_adopted(self, animal_id: str, adopter_name) -> None:
        if not self.is_adopted(animal_id) and animal_id in self.animals:
            self.adoptions[animal_id] = adopter_name


if __name__ == '__main__':

    animal1: Cat = Cat(id='#1', name='Garfield', age_years=3, weight_kg=5.1, favourite_toy='ball', indoor_only=True)
    animal2: Cat = Cat(id='#2', name='Tom', age_years=4, weight_kg=3.5, favourite_toy='mouse', indoor_only=False)
    animal3: Dog = Dog(id='#3', name='Spike', age_years=1, weight_kg=5, breed='bool dog', is_trained=True)
    animal4: Dog = Dog(id='#4', name='Spek', age_years=8, weight_kg=10.1, breed='russel', is_trained=True)


    shelter1: Shelter = Shelter()

    shelter1.add_animal(animal=animal1)
    shelter1.add_animal(animal=animal2)
    shelter1.add_animal(animal=animal3)
    shelter1.add_animal(animal=animal4)

    print(shelter1.list_all())