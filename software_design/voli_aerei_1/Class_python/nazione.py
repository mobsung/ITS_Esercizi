


class Nazione:

    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f'Nation name: {self._name}'
    
    def getName(self) -> str:
        return self._name