from __future__ import annotations


class Student:

    _name: str # <<imm>>, si conosce alla nascita
    _esami: set[_esame]

    def __init__(self, name: str) -> None:
        self._name = name
        self._esami = set()

    def name(self) -> str:
        return self._name
    
    def add_esame(self, voto: int, modulo: Modulo) -> None:
        esame: _esame = _esame(voto=voto, student=self, modulo=modulo)

        if esame in self.esami():
            raise ValueError('L\'esame è satato già fatto')

        self._esami.add(esame)

    def esami(self) -> frozenset[_esame]:
        return frozenset[self._esami]
    
    def media(self) -> float:

        voti: float = 0

        for esame in self._esami:
            voti += esame.voto()
        
        return voti / len(self._esami)
    
    def __str__(self) -> str:
        return f'Student name: {self.name()}, Esami: {self.esami()}'


class Modulo:

    _id: str # <<imm>>, si conosce alla nascita

    def __init__(self, id: str) -> None:
        self._id = id

    def id(self) -> str:
        return self._id
    

class _esame:

    _voto: int # <<imm>> 
    _student: Student # <<imm>>
    _modulo: Modulo # <<imm>>

    def __init__(self, voto: int, student: Student, modulo: Modulo) -> None:
       self._voto = voto
       self._student = student
       self._modulo = modulo

    def voto(self) -> int:
        return self._voto
    
    def student(self) -> Student:
        return self._student
    
    def modulo(self) -> Modulo:
        return self._modulo
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        else:
            return self.student() == other.student() and self.modulo() == other.modulo()

    def __hash__(self):
        return hash((self.student(), self.modulo()))
        
    
    def __str__(self):
        return f'Studente: {self.student()}, Modulo: {self.modulo()}, Voto: {self.voto()}'
    

if __name__ == '__main__':

    modulo1: Modulo = Modulo(id='A123')
    
    stud1: Student = Student(name='Fool')

    stud1.add_esame(voto=30, modulo=modulo1)
    stud1.add_esame(voto=25, modulo=modulo1)
    print(stud1)
    print(stud1.media())