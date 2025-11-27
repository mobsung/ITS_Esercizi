from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from custom_types import RealGZ, IntGEZ


class PostOggetto(ABC):

    _descrizione: str
    _prezzo: RealGZ
    _anni_garanzia: IntGEZ
    _pubblicazione: datetime # <<imm>>
    #_is_nuovo: bool # <<imm>>


    @abstractmethod
    def __init__(self, descrizione: str, prezzo: RealGZ, pubblicazione: datetime, anni_garanzia: IntGEZ) -> None:
        self.set_descrizione(descrizione)
        self.set_prezzo(prezzo)
        self.set_pubblicazione(pubblicazione)
        self.set_anni_garanzia(anni_garanzia)
        #self.set_condizioni(is_nuovo)


    def set_descrizione(self, descrizione) -> None:
        if descrizione:
            self._descrizione = descrizione

    def set_prezzo(self, prezzo: RealGZ) -> None:
        if prezzo: # verifica se prezzo non è vuoto 
            self._prezzo = prezzo

    def set_pubblicazione(self, pubblicazione: datetime) -> None:
        if pubblicazione:
            self._pubblicazione = pubblicazione

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self._anni_garanzia = anni_garanzia

    def descrizione(self) -> str:
        return self._descrizione
    
    def prezzo(self) -> RealGZ:
        return self._prezzo
    
    def anniGaranzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione