'''
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
 
Codice driver
Crea un'istanza della classe MovieCatalog.
Aggiungi nuovi film e registi.
Aggiungi film a registi già presenti nel catalogo.
Rimuovi film dal catalogo.
Elenca i registi presenti nel catalogo.
Visualizza film di uno specifico regista.
Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.
'''

import re

class MovieCatalog():

    def __init__(self):
        
        self.movie_catalog: dict[str, str] = {}


    def add_movie(self, director_name: str, movies: list[str]) -> None:

        for movie in movies:

            if director_name not in self.movie_catalog:
                self.movie_catalog[director_name] = movies
            
            elif director_name in self.movie_catalog and movie not in self.movie_catalog[director_name]:
                self.movie_catalog[director_name] += [movie]


    def remove_movie(self, director_name: str, movie_name: str) -> None:

        if director_name in self.movie_catalog:
            if movie_name in self.movie_catalog[director_name]:
                self.movie_catalog[director_name].remove(movie_name)
            
            else:
                print(f'The movie "{movie_name}" can\'t be found in the catalog!\n')

        else:
            print(f'The director "{director_name}" can\'t be found in the catalog!\n')


    def list_directors(self):

        directors: str = "-- Directors --\n"

        for index, director in enumerate(self.movie_catalog):

            if len(self.movie_catalog) > 0:
                directors += f'{index + 1} - "{director}"\n'

            else:
                director += f'There aren\'n any Directors in the catalog yet!\n'

        print(f'{directors}')


    def get_movies_by_director(self, director_name):

        if director_name in self.movie_catalog:
            director_movies = f'-- Movies by the Director "{director_name}" --\n'
            for index, movie in enumerate(self.movie_catalog[director_name]):

                director_movies += f'{index + 1} - {movie}\n'

            print(f'{director_movies}')

        else:
            print(f'The director "{director_name}" can\'t be found in the Movie catalog!')


    def search_movies_by_title(self, title):

        director_title: str = "-- Directors by Title --\n"

        for director, movies in self.movie_catalog.items():
            
            for movie in movies:

                if re.search(fr'\b{title}\b', str(movie)):
                    director_title += f'{director} - {movie}\n'
                
        if director_title == "-- Directors by Title --\n":
            print(f'The title "{title}" can\'t be found in the Movie Catalog!\n')
        else:
            print(director_title)
                


if __name__ == "__main__":

    movie_catalog: MovieCatalog = MovieCatalog()

    movie_catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Tenet", "Dunkirk"])

    movie_catalog.add_movie("Steven Spielberg", ["E.T.", "Jurassic Park", "Pulp"])

    movie_catalog.add_movie("Quentin Tarantino", ["Pulp Fiction"])

    movie_catalog.add_movie("Christopher Nolan", ["Oppenheimer"])

    movie_catalog.remove_movie("Christopher Nolan", "Inception")
    movie_catalog.remove_movie("Christopher Nolan", "Avatar")

    movie_catalog.list_directors()

    movie_catalog.get_movies_by_director("Christopher Nolan")

    movie_catalog.search_movies_by_title("Pulp")
    movie_catalog.search_movies_by_title("BLA")