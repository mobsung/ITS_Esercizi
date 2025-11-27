from __future__ import annotations
from typing import TYPE_CHECKING, Any
from datetime import datetime
import weakref

if TYPE_CHECKING:
    from asta import Asta
    from bid import Bid

class Asta_Bid:

    @classmethod
    def add(cls, asta: Asta, bid: Bid) -> None:
        link = Asta_Bid._link(asta, bid)
        asta.add_link_asta_bid(link)
        bid.add_link_asta_bid(link)
           
    class _link:

        _asta: Asta
        _bid: Bid

        def __init__(self, asta: Asta, bid: Bid):
            self._asta = asta
            self._bid = bid
            
        def asta(self) -> Asta:
            return self._asta

        def bid(self) -> Bid:
            return self._bid

        def __repr__(self):
            return f"Asta_Bid (Asta={self._asta}, Bid={self._bid}, Istante={self._bid._istanteBid().isoformat()})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Asta_Bid._link) and self._asta == other._asta and self._bid == other._bid
                )