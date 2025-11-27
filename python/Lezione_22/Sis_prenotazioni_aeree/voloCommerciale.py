'''
Classe VoloCommerciale:
Estende la classe Volo e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. Il costruttore deve inoltre gestire i seguenti attributi interi: posti_economica, posti_business, e posti_prima; i quali consentono di stabilire quanti posti sono stati riservati alla classe economica, quanti alla classe business e quanti alla prima classe su ogni volo. Il costruttore non deve ricevere in input questi argomenti, ma assegnare loro un valore iniziale tale che la somma di questi tre valori interi sia uguale al numero dei posti disponibili sul volo. Si può pensare di riservare il 70% dei posti alla classe economica, il 20% dei posti alla classe business ed i restanti posti alla prima classe. Inoltre, il costruttore deve creare tre valori interi pari a 0, chiamati prenotazioni_economica, prenotazioni_business, prenotazioni_prima.
 
Metodi:

    posti_disponibili(): che ritorna un dizionario in cui vengono salvati il numero di posti disponibili totali sul volo nel seguente modo: il dizionario deve avere quattro chiavi, ovvero, 'posti disponibili',  'classe business', 'prima classe'. Alla chiave 'posti disponibili' associare come rispettivo valore il numero di posti disponibili rimasti sul volo, alla 'classe economica',chiave 'classe economica' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella classe economica, alla chiave 'classe business' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella classe business, alla chiave 'prima classe' associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe. Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore da associare alla corrispondete chiave è 0.

    prenota_posto(posti, classe_servizio): che consente di prenotare un certo numero di posti sul volo in una determinata classe. Tale metodo, prima di riservare un posto, deve controllare prima che ci siano posti disponibili sull'intero volo, poi se ci sono posti disponibili nella classe richiesta. In caso affermativo, contare il numero dei posti prenotati in tale classe. Inoltre, nel caso in cui sia possibile prenotare un posto, il metodo deve stampare a schermo un messaggio che notifichi all'utente di aver riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo). In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. Se sul volo non ci sono più posti disponibili, il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo. Inoltre, se la classe passata come input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"), il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida. Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni ricevute per ogni classe di servizio, poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con l'esatto numero delle prenotaioni ricevute per ogni classe di servizio. Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di servizio da azzerare all'inizio di ogni fase di prenotazione.
'''
# print(f'Hai prenotato {posti} posti di tipologia {classe_servizio} del volo {self.codice_volo()}!')
# print(f'Non ci sono abbastanza posti disponibili nella classe {classe_servizio}!')
# print('Il volo è completo!')
# print(f'La classe {classe_servizio} non esiste!')


from volo import Volo



class VoloCommerciale(Volo):

    posti_rimanenti: int
    posti_ecconomica: int
    posti_business: int
    posti_prima: int
    ecconomica_prenotati: int
    business_prenotati: int
    prima_prenotati: int


    def __init__(self, codice_volo: str, cap_massima: int) -> None:
        super().__init__(codice_volo, cap_massima)
        self.posti_rimanenti = self.capacitaMassima()
        self.posti_ecconomica = int(self.capacitaMassima() * 0.7)
        self.posti_business = int(self.capacitaMassima() * 0.2)
        self.posti_prima = self.capacitaMassima() - self.posti_ecconomica - self.posti_business
        self.ecconomica_prenotati = 0
        self.business_prenotati = 0
        self.prima_prenotati = 0


    def prenota_posto(self, posti: int, classe_servizio: str) -> None:
        if classe_servizio in self.posti_disponibili():
            if posti <= self.posti_rimanenti:
                if posti <= self.posti_disponibili()[classe_servizio]:
                    print(f'Hai prenotato {posti} posti di tipologia {classe_servizio} del volo {self.codiceVolo()}!')
                    self.posti_rimanenti -= posti
                    if classe_servizio == 'ecconomica':
                        self.posti_ecconomica -= posti
                        self.ecconomica_prenotati += posti
                    if classe_servizio == 'business':
                        self.posti_business -= posti
                        self.business_prenotati += posti
                    if classe_servizio == 'prima':
                        self.posti_prima -= posti
                        self.prima_prenotati += posti
                    self.prenotazioni += posti
                else:
                    print(f'Non ci sono abbastanza posti disponibili nella classe {classe_servizio}!')
            else:
                print('Il volo è completo!')
        else:
            print(f'La classe {classe_servizio} non esiste!')

    def posti_disponibili(self) -> dict[str, int]:
        posti_disponibili: dict[str, int] = {

            'posti disponibili': self.posti_rimanenti,
            'ecconomica': self.posti_ecconomica,
            'business': self.posti_business,
            'prima': self.posti_prima

        }
        return posti_disponibili

    
    

if __name__ == '__main__':

    vCom: VoloCommerciale = VoloCommerciale(codice_volo='COM123', cap_massima=100)

    print(vCom.posti_disponibili())
    vCom.prenota_posto(posti=50, classe_servizio='ecconomica')
    print(vCom.posti_disponibili())
