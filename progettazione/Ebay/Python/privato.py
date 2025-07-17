from __future__ import annotations
from utente import Utente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bid_ut import Bid_Ut

class Privato(Utente):

    _ruolo: str
    _link_bid: set[Bid_Ut._link]

    def __init__(self, username: str) -> None:
        super().__init__(username)
        self._ruolo = "Privato"
        self._link_bid: set[Bid_Ut._link] = set()

    def ruolo(self) -> str:
        return self._ruolo

    def add_link_bid_ut(self, link: Bid_Ut._link) -> None:
        if link.utente() is not self:
            raise ValueError("Impossibile aggiumgere il link in quanbto inerente ad un'utente diverso!\n")
        self._link_bid.add(link)

    def __repr__(self):
        return f"Username: {self.username()}\nData registrazione: {self.registrazione()}\nTipologia Utente: {self._ruolo}"

    