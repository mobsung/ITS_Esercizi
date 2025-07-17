from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from index import Index
from typing import Self

class Utente(ABC):

    index_username = Index[str, "Self"]("Registered")

    _username: str # <<imm>>
    _registrazione: datetime  # <<imm>>


    def __init__(self, user: str) -> None:
        if self.index_username.get(user) is not None:
            raise ValueError(f'Username: {user} già registrato!\n')
        self._username = user
        self._registrazione = datetime.now()
        self.index_username.add(user, self)

    def username(self) -> str:
        return self._username

    def registrazione(self) -> datetime:
        return self._registrazione

    def remove_registrazione(self) -> None:
        self.index_username.remove(self.username())

    def __str__(self):
        return self.get_username()

    def __repr__(self) -> str:
        return f"Username: {self.username()}\nData: {self.registrazione().isoformat()}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Utente) and self.username() == other.username()

    def __hash__(self):
        return hash(self.username())

        