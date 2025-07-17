from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utente import Utente
    from bid_ut import Bid_Ut
    from asta_bid import Asta_Bid

class Bid:
    _istanteBid: datetime
    _utente: Utente
    _link_bid: set[Bid_Ut._link]
    _link_bid_asta: set[Asta_Bid._link]

    def __init__(self, utente: Utente):
        self._istanteBid = datetime.now()
        self._utente = utente
        self._link_bid: set[Bid_Ut._link] = set()
        self._link_bid_asta: set[Asta_Bid._link] = set()

    def istanteBid(self) -> datetime:
        return self._istanteBid

    def utente(self) -> Utente:
        return self._utente

    def add_link_bid_ut(self, link: 'Bid_Ut._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.\n")
        self._link_bid.add(link)

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.\n")
        self._link_bid_asta.add(link)

    def __repr__(self):
        return f"Username:{self._utente.username()},Data Bid: {self._istanteBid.isoformat()}"

    