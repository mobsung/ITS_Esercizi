from myTypes import IntG1900


class CompagniaAerea:

    _name: str
    _anno_fondazione: IntG1900 # <<immutable>>

    def __init__(self, name: str, anno_fondazione: int | IntG1900 | str | bool | float) -> None:
        self._name = name
        _mod_year: bool = False # variabile che se impostata a True non permette di modificare l'anno di fondazione
        if _mod_year == False:
            _mod_year = True
            self._anno_fondazione = IntG1900(anno_fondazione)

    def __str__(self) -> str:
        return f'Company name: {self._name} - Foundation year: {self._anno_fondazione}'
    
    def getName(self) -> str:
        return self._name
    
    def getAnnoFondazione(self) -> str:
        return self._anno_fondazione