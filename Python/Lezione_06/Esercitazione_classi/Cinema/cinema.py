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

from sala import *

class Cinema:

    lista_sale: list = []

    def aggiungi_sala(self, sala: Sala) -> None:
        self.lista_sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.lista_sale:
            if titolo_film == sala.getFilm().getTitle():
                print('--> Film trovato')
                if sala.prenota_posti(num_posti):
                    return '--> Prenotazione effettauta correttamente'
                else:
                    return '--> Prenotazione non andata a buon fine'
        return '--> Film non trovato'