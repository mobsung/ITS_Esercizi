'''
1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."
'''

class Movie:

    movie_id: str
    title: str
    director: str
    is_rented: bool

    def __init__(self, movie_id: str, title: str, director: str):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self) -> None:
        if self.is_rented == False:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self) -> None:
        if self.is_rented == True:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")