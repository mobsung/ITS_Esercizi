
from custom_types import *

class Persona:

    _nome: str # <<mutabile>>
    _cognome: str # <<mutabile>>
    _cf: CodiceFiscale # <<mutabile>>
    _data_nascita: date # <<imm>>
    _maternita: IntGEZ | None # [0..1] <mutabile>>
    _pos_militare: str | None # [0..1] <mutabile>>
    _is_uomo: bool # <<mutabile>>
    _is_donna: bool # <<mutabile>>


    def __init__(self, *, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, maternita: IntGEZ | None, pos_mil: str | None) -> None:
        self.setNome(nome)
        self.setCognome(cognome)
        self.setCf(cf)
        self._setNascita(nascita)
        self.setDonna(maternita)
        self.setUomo(pos_mil)

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def cf(self) -> CodiceFiscale:
        return self._cf
    
    def data_nascita(self) -> date:
        return self._data_nascita
    
    def maternita(self) -> IntGEZ:
        return self._maternita
    
    def pos_militare(self) -> str:
        return self._pos_militare
    
    def is_uomo(self) -> bool:
        return self._is_uomo
    
    def is_donna(self) -> bool:
        return self._is_donna

    def setNome(self, nome: str) -> None:
        if nome:
            self._nome = nome

    def setCognome(self, cognome: str) -> None:
        if cognome:
            self._cognome = cognome

    def setCf(self, cf: CodiceFiscale) -> None:
        if cf:
            self._cf = cf

    def _setNascita(self, data_nascita: date) -> None:
        if data_nascita:
            self._data_nascita = data_nascita        