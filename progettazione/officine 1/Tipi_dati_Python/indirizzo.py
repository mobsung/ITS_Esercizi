import re

class Indirizzo:

    pattern_cap = re.compile(r'[0-9]{5}')

    def __init__(self, via: str, civico: str, cap: str):
        self.setIndirizzo(via, civico, cap)

    def setIndirizzo(self, via: str, civico: str, cap: str) -> None:
        if type(via) == str and type(civico) == str and re.fullmatch(self.pattern_cap, cap):
            self.via = via
            self.civico = civico
            self.cap = cap
        else: 
            raise ValueError('Indirizzo non valido')
        
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.via == other.via and self.civico == other.civico and self.cap == other.cap

    def __hash__(self):

        return hash((self.via, self.civico, self.cap))
    

if __name__ == '__main__':

    indirizzo_1: Indirizzo = Indirizzo('Via domenico Sfondrini', '5', '00132')
    indirizzo_2: Indirizzo = Indirizzo('Via domenico Sfondrini', '5', '00132')
    indirizzo_3: Indirizzo = Indirizzo('Via Saponara', '12', '00128')

    print({indirizzo_1, indirizzo_2, indirizzo_3})