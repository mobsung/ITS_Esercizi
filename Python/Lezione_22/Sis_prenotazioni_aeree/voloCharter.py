'''
Classe VoloCharter:
Estende la classe Volo e e definisce gli attributi codice del volo e capacità massima di posti disponibili sul volo. Il costruttore deve inoltre gestire il costo del volo (numero float) per il charter. Un volo charter è un volo di cui tutti i posti disponibili vengono acquistati tutti insieme in una sola volta da un tour operator ad un certo prezzo.
 
Metodi:

    prenota_posto(): questo metodo verifica che se l'aereo è vuoto, ovvero i posti disponibili sono pari alla capacità massima di posti. In quel caso, è possibile prenotare un numero di posti pari alla capacità massima di posti supportata dal volo. Nel caso in cui la prenotazione charter andasse a buon fine, il metodo deve stampare a schermo un messaggio in cui avvisa il tour operator che il volo charter (specificandone il codice del volo) è stato prenotato completamente, mostrando anche il prezzo pagato. In caso contrario, il metodo deve mostrare un messaggio a schermo in cui avvisa l'utente che il volo charter è gia prenotato.

    posti_disponibili(): che ritorna il numero di posti disponibili totali sul volo.
'''

from volo import Volo


class VoloCharter(Volo):

    costo_volo: float
    posti_rimanenti: int

    def __init__(self, codice_volo: str, cap_massima: int, costo_volo: float) -> None:
        super().__init__(codice_volo, cap_massima)
        self.costo_volo = costo_volo
        self.posti_rimanenti = self.capacitaMassima()

    def prenota_posto(self, posti: int) -> None:
        if posti:
            if posti == self.posti_disponibili():
                print(f'Il volo con codice "{self.codiceVolo()}" è stato prenotato correttamente per un prezzo totale di ${self.costoVolo()}!')
                self.posti_rimanenti = 0
            else:
                print('I posti prenotati non sono idonei per ricoprire quelli offerti!')

    def posti_disponibili(self) -> int:
        return self.posti_rimanenti
    
    def costoVolo(self) -> float:
        return self.costo_volo
    


if __name__ == '__main__':

    vCom: VoloCharter = VoloCharter(codice_volo='COM123', cap_massima=100, costo_volo=10000)

    print(vCom.posti_disponibili())
    vCom.prenota_posto(posti=100)
    print(vCom.posti_disponibili())