import re

class NumeroTelefono:

    pattern_telefono = re.compile(r'((00|\+)39[\. ]??)??3\d{2}[\. ]??\d{6,7}')

    def __init__(self, numero_telefono: str):
        self._setNumeroTelefono(numero_telefono)

    def _setNumeroTelefono(self, numero_telefono: str) -> None:
        if re.fullmatch(self.pattern_telefono, numero_telefono):
            self.numero_telefono = numero_telefono
        else:
            raise ValueError('Numero di telefono indicato non valido')
        
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.numero_telefono == other.numero_telefono

    def __hash__(self):

        return hash((self.numero_telefono))