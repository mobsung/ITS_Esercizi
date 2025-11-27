from __future__ import annotations
import datetime

class Impiegato:

    _nome: str
    _cognome: str
    _data_nascita: datetime.date
    _stipendio: float
    _progetti: set[_partecipa]


    def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, stipendio: float) -> None:
        self._nome = nome
        self._cognome = cognome
        self._data_nascita = data_nascita
        self._stipendio = stipendio
        self._progetti = set()
        
    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def data_nascita(self) -> datetime.date:
        return self._data_nascita
    
    def stipendio(self) -> float:
        return self._stipendio
    
    def progetti(self) -> frozenset[_partecipa]:
        return frozenset[self._progetti]
    
    def add_progetto(self, data_inizio: datetime.date, progetto: Progetto) -> None:
        partecipa: _partecipa = _partecipa(data_inizio=data_inizio, progetto=progetto, impiegato=self)
        self._progetti.add(partecipa)
        for part in progetto._impiegati:
            if self != partecipa.progetto():
                print('creato da prog')
                progetto.add_impiegato(data_inizio=data_inizio, progetto=progetto, impiegato=self)

    def __str__(self):
        return f'Nome: {self.nome()}, Progetti: {self.progetti()}'
        


class Progetto:

    _nome: str # noto alla nascita
    _budget: float # noto alla nascita
    _impiegati: set[_partecipa] # certamente non noto alla nascita

    def __init__(self, nome: str, budget: float) -> None:
        self._nome = nome
        self._budget = budget
        self._impiegati = set()

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> float:
        return self._budget
    
    def impiegati(self) -> frozenset[_partecipa]:
        return frozenset[self._impiegati]
    
    def add_impiegato(self, data_inizio: datetime.date, impiegato: Impiegato) -> None:
        partecipa: _partecipa = _partecipa(data_inizio=data_inizio, progetto=self, impiegato=impiegato)
        self._impiegati.add(partecipa)
        for part in impiegato.progetti():
            if self != partecipa.progetto():
                print('creato da imp')
                impiegato.add_progetto(data_inizio=data_inizio, progetto=self, impiegato=impiegato)

    def __str__(self):
        return f'Nome: {self.nome()}, Impiegati: {self.impiegati()}'
        


class _partecipa:

    _data_inizio: datetime.date # <<imm>>
    _progetto: Progetto # <<imm>> certamente noti alla nascita
    _impiegato: Impiegato # <<imm>> certamente noto alla nascita

    def __init__(self, data_inizio: datetime.date, progetto: Progetto, impiegato: Impiegato) -> None:
        self._data_inizio = data_inizio
        self._progetto = progetto
        self._impiegato = impiegato

    def data_inizio(self) -> datetime.date:
        return self._data_inizio
    
    def progetto(self) -> Progetto:
        self._progetto

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def __hash__(self):
        return hash((self.progetto(), self.impiegato()))
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        else:
            return self.progetto() == other.progetto() and self.impiegato() == other.impiegato()
    
    def __repr__(self):
        return f'"{self.progetto()}", "{self.impiegato()}", "{self.data_inizio()}"'
    
if __name__ == '__main__':

    progetto: Progetto = Progetto(nome='Pegaso', budget=30000)
    impiegato: Impiegato = Impiegato(nome='Fool', cognome='The', data_nascita=1, stipendio=1000)

    progetto.add_impiegato(data_inizio=2, impiegato=Impiegato)
    #impiegato.add_progetto(data_inizio=2, progetto=progetto)

    print(progetto)
    print(impiegato)