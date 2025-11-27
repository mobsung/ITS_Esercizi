'''
Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore. Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
'''

from forma import Forma

class Quadrato(Forma):

    lato: int

    def __init__(self, lato: int) -> None:
        self.name = 'Quadrato'
        self.lato = lato

    def getArea(self) -> int:
        return self.lato ** 2
    
    def render(self):
        
        print('* ' * self.lato)
        for _ in range(self.lato - 2):
            print(f"*{' ' * (self.lato + (self.lato - 3))}*")
        print('* ' * self.lato)
        

if __name__ == '__main__':

    obj1: Quadrato = Quadrato(lato=6)

    obj1.render()