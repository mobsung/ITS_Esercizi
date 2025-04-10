

from persona import Persona
from typing import Any

class Studente(Persona):

    '''
    attributi ereditati dalla classe Persona
        self.name
        self.last_name
        self.age

    attributi della classe Studente
        self.matricola
    '''

    def __init__(self, name:str = "", last_name:str = "", age:int = 0, matricola:str = ""):
        super().__init__(name, last_name, age)

        self.setMatricola(matricola)
    

    def setMatricola(self, matricola:str) -> None:

        self.matricola = matricola


    def getMatricola(self) -> str:

        return self.matricola


    def __str__(self):

        return f'Nome: {self.getName()}\nLast name: {self.getLastName()}\nMatricola: {self.matricola}\n{20 * "-"}'
    

    def __call__(self):

        print(f'{self.getName()} {self.getLastName()} ha superato le selezioni!\n{20 * "-"}')
    

    def getMediaEsami(self, voti_esami:list[int]) -> float:

        if voti_esami:
            somma:int = sum(voti_esami)
        
            print(f'La media dello studente con matricola: {self.getMatricola()} è {round(somma/len(voti_esami), 2)}\n{20 * "-"}')
    
        else:
            print(f'La media dello studente con matricola: {self.getMatricola()} è 0.00\n{20 * "-"}')

    
    #metodo che consente di confrontare due oggetti della stessa classe per verificarne l'uguaglianza
    def __eq__(self, other:Any):
        
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.getMatricola() == other.getMatricola()
            

if __name__ == "__main__":

    marcel:Studente = Studente()

    print(marcel)

    marcel.setName("Marcel")
    marcel.setLastName("Movileanu")
    marcel.setAge(24)
    marcel.setMatricola("12345")


    print(marcel)

    marcel()