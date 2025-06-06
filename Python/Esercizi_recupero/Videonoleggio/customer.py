'''
2. Classe Customer:
Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."
'''

from movie import Movie

class Customer:

    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id: str = customer_id
        self.name: str= name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie not in self.rented_movies:
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")

    def return_movie(self, movie: Movie) -> None:
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

    def get_movies(self) -> list[Movie]:
        return self.rented_movies