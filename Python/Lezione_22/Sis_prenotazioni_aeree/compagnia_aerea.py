'''
Classe CompagniaAerea:
Questa classe deve avere un costruttore che richiede come argomento in input solo il nome della compagnia (stringa) ed il prezzo standard di un biglietto (numero float), e creare una lista vuota chiamata flotta. La classe CompagniaAerea deve gestire molteplici voli commerciali, attraverso i seguenti metodi:
aggiungi_volo(volo_commericiale): il volo_commerciale deve essere aggiunto alla flotta della compagnia aerea.
rimuovi_volo(volo_commericiale): il volo_commerciale deve essere rimosso dalla flotta della compagnia aerea.
mostra_flotta(): tale metodo deve stampare a schermo tutti i voli che fanno parte della flotta della compagnia aerea, specificando il codice di ogni volo.
guadagno(): questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali) il gadagno ricavato dalla vendita dei biglietti aerei dei voli nella sua flotta. Su ogni aereo della flotta, il prezzo  per un posto in classe economica è pari a prezzo standard, il prezzo per un posto in classe business è pari al doppio del prezzo standard, mentre il prezzo per un posto in prima classe vale tre volte il prezzo standard.
'''
from voloCommerciale import VoloCommerciale

class CompagniaAerea:

    nome: str
    prezzo: float
    flotta: list[VoloCommerciale]

    def __init__(self, nome: str, prezzo: float) -> None:
        self.nome = nome
        self.prezzo = prezzo
        self.flotta = []

    def aggiungi_volo(self, volo_commericiale: VoloCommerciale):
        if volo_commericiale:
            if volo_commericiale not in self.flotta:
                self.flotta.append(volo_commericiale)
    
    def rimuovi_volo(self, volo_commericiale: VoloCommerciale):
        if volo_commericiale:
            if volo_commericiale in self.flotta:
                self.flotta.remove(volo_commericiale)

    def mostra_flotta(self):
        flotta: str = f"{'\n'.join([volo.codiceVolo() for volo in self.flotta])}"
        return flotta

    def guadagno(self):
        guadagno: float = 0
        for volo in self.flotta:
            guadagno += (volo.ecconomica_prenotati * self.prezzo + volo.business_prenotati * (2 * self.prezzo) + volo.prima_prenotati * (3 * self.prezzo))  
        return guadagno

if __name__ == '__main__':

    CA: CompagniaAerea = CompagniaAerea(nome='Pegasus', prezzo=10)

    vCom1: VoloCommerciale = VoloCommerciale(codice_volo='COM123', cap_massima=100)
    vCom2: VoloCommerciale = VoloCommerciale(codice_volo='ZSE234', cap_massima=200)
    vCom3: VoloCommerciale = VoloCommerciale(codice_volo='FRT345', cap_massima=300)
    vCom4: VoloCommerciale = VoloCommerciale(codice_volo='HSS456', cap_massima=400)
    vCom5: VoloCommerciale = VoloCommerciale(codice_volo='VPP567', cap_massima=500)
    vCom1.prenota_posto(posti=10, classe_servizio='business')
    print(vCom1.posti_disponibili())

    CA.aggiungi_volo(vCom1)
    CA.aggiungi_volo(vCom2)
    CA.aggiungi_volo(vCom3)
    CA.aggiungi_volo(vCom4)
    CA.aggiungi_volo(vCom5)

    print(CA.mostra_flotta())
    print(CA.guadagno())