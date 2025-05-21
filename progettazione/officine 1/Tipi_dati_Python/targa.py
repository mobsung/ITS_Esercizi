import re

class Targa:

    pattern_targa = re.compile(r'[A-Z]{2}[0-9]{3}[A-Z]{2}')

    def __init__(self, targa:str):
        self.setTarga(targa)

    def setTarga(self, targa:str) -> None:
        if re.fullmatch(self.pattern_targa, targa):
            self.targa = targa
        else:
            raise ValueError('La targa inserita è errata')
        
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.targa == other.targa

    def __hash__(self):

        return hash((self.targa))
    
if __name__ == '__main__':

    targa1: Targa = Targa('AB123CD')
    targa2: Targa = Targa('AB123CD')
    targa3: Targa = Targa('EF456GH')

    print({targa1, targa2, targa3})