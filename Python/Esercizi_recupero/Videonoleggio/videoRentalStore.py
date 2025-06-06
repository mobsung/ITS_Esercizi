'''
3. Classe VideoRentalStore:
Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.
Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."

● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."

● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."

● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."

● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.
'''

from customer import *

class VideoRentalStore:

    def __init__(self):
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id=movie_id, title=title, director=director)
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")

    def register_customer(self, customer_id: str, name: str) -> None:
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id=customer_id, name=name)

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self.customers:
            if movie_id in self.movies:
                self.movies[movie_id].rent()
                self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self.customers:
            if movie_id in self.movies:
                self.movies[movie_id].return_movie()
                self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].get_movies()
        else:
            print("Cliente non trovato.")
            return []