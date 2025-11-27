'''
Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
'''

from forma import Forma

class Rettangolo(Forma):


    lunghezza: int
    altezza: int

    def __init__(self, lunghezza: int, altezza: int) -> None:
        self.name = 'Rettangolo'
        self.lunghezza = lunghezza
        self.altezza = altezza

    def getArea(self) -> int:
        return self.lunghezza * self.altezza
    
    def render(self):
        
        print('* ' * self.lunghezza)
        for _ in range(self.altezza - 2):
            print(f"*{' ' * (self.lunghezza + (self.lunghezza - 3))}*")
        print('* ' * self.lunghezza)

if __name__ == '__main__':

    obj1: Rettangolo = Rettangolo(lunghezza=9, altezza=3)

    obj1.render()