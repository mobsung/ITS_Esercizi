from myTypes import CodiceAeroporto


class Aeroporto:

    _codice_aeroporto: CodiceAeroporto # <<immutable>>
    _name: str

    def __init__(self, name: str, codice_volo: str | CodiceAeroporto) -> None:
        self.name = name
        self._codice_aeroporto = CodiceAeroporto(codice_volo)

    def getNome(self) -> str:
        return self.name
    
    def setName(self, name: str) -> None:
        self.name = name