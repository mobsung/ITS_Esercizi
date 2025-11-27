'''
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
Metodi:

    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
Metodi:

    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
Test case:
Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
Un cliente sceglie un film e prenota un certo numero di posti.
Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
'''

from film import Film

class Sala:

    def __init__(self, code: str, film: Film, posti: int):
        self.code = code
        self.film = film
        self.posti = posti

    def prenota_posti(self, num_posti: int) -> bool:
        if self.posti - num_posti < 0:
            print('--> Non ci sono posti a sufficienza')
            return False
        else:
            self.posti -= num_posti
            print('--> Posti disponibili')
            return True
        
    def getPosti(self) -> int:
        return self.posti
    
    def getFilm(self) -> Film:
        return self.film