from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from bid import Bid
    from privato import Privato

class Bid_Ut:

    @classmethod
    def add(cls, u: Privato, b: Bid) -> None:
        link = Bid_Ut._link(u, b)
        u.add_link_bid_ut(link)
        b.add_link_bid_ut(link)

    class _link:

        _utente: Privato
        _bid: Bid

        def __init__(self, utente: Privato, bid: Bid):
            self._utente = utente
            self._bid = bid

        def utente(self) -> Privato:
            return self._utente

        def bid(self) -> Bid:
            return self._bid

        def __repr__(self):
            return f"Bid_Ut (Utente={self._utente}, Bid={self._bid})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Bid_Ut._link) and self._utente == other._utente and self._bid == other._bid
            )