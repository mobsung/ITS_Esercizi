'''
Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore. Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
'''

from forma import Forma

class Triangolo(Forma):

    lato: int

    def __init__(self, lato: int) -> None:
        self.name = 'Triangolo'
        self.lato = lato

    def getArea(self) -> float:
        return (self.lato ** 2) / 2
    
    def render(self):
        
        for i in range(self.lato):
            if i == 0:
                print("*")
            elif i == self.lato - 1:
                print("* " * self.lato)
            else:
                print("* " + "  " * (i - 1) + "*")
        

if __name__ == '__main__':

    obj1: Triangolo = Triangolo(lato=4)

    obj1.render()