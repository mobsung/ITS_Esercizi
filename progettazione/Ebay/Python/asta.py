from __future__ import annotations
from datetime import datetime
from custom_types import RealGZ, IntGEZ
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bid import Bid
    from asta_bid import Asta_Bid
    from utente import Utente
    from postOggetto import PostOggetto

class Asta(PostOggetto):

    _prezzo_bid: RealGZ
    _scadenza: datetime
    _insieme_bid: set['Bid']
    _link_bid: set['Asta_Bid._link']


    def __init__(self, descrizione: str, prezzo: RealGZ, pubblicazione: datetime, anni_garanzia: IntGEZ, prezzo_bid: RealGZ, scadenza: datetime) -> None:
        super().__init__(descrizione, prezzo, pubblicazione, anni_garanzia)
        if pubblicazione >= scadenza:
            raise ValueError("L'istante scadenta deve essere maggiore all'istante di pubblicazione!\n")
        self.set_scadenza(scadenza)
        self.set_prezzo(prezzo)
        self.set_prezzo_bid(prezzo_bid)
        self._insieme_bid: set['Bid'] = set()
        self._link_bid: set['Asta_Bid._link'] = set()
        
    def set_prezzo(self, prezzo: RealGZ) -> None:
        if prezzo is not None:
            if prezzo: # verifica se prezzo non è vuoto 
                if self.is_scaduta() or self._link_bid:
                    raise ValueError("Impossibile cambiare il 'prezzo' in quanto l'asta è scaduta oppure è avvenuto un bid!\n")
                self._prezzo = prezzo

    def set_prezzo_bid(self, prezzo_bid: RealGZ) -> None:
        if prezzo_bid is not None:
            if prezzo_bid: # verifica se prezzo_bid non è vuoto 
                if self.is_scaduta() or self._link_bid:
                    raise ValueError("Impossibile cambiare il 'prezzo del bid' in quanto l'asta è scaduta oppure è avvenuto un bid!\n")
                self._prezzo_bid = prezzo_bid 
            
    def set_scadenza(self, scadenza: datetime) -> None:
        if self.is_scaduta() or self._link_bid:
            raise ValueError ("Non è possibile cambiare la scadenza in quanto l'asta è finita oppure è avvenuto un bid!\n")
        if scadenza < datetime.now():
            raise AttributeError("L'istante della scadenza deve essere maggiore all'istante attuale!\n")
        self._scadenza = scadenza
        
    def aggiungi_bid(self, bid: 'Bid') -> None:
        if bid.IstanteBid() > self._scadenza:
            raise ValueError("Impossibile registrare il bid in quanto effettuato dopo la scadenza dell'asta!\n")
        if bid in self._insieme_bid:
            raise ValueError("Il bid inserito è stato già registrato!\n")
        self._insieme_bid.add(bid)

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.asta() is not self:
            raise ValueError("Impossibile inserire il link in quanto effettuato verso un'asta diversa!\n")
        self._link_bid.add(link)

    def is_scaduta(self) -> bool:
        return datetime.now() > self._scadenza
    
