'''
Sul banco, le fiale vanno prelevate nell'ordine inverso all'inserimento. Fai sì che il testo lo comandi: `Stack` con `push(x)`, `pop()` (solleva **`IndexError`** se vuoto) e `is_empty()`. Mantieni la firma data e fai superare tutti i test automatici.
'''

class Stack:
    
    def __init__(self) -> None:
        self.lst = []

    def push(self, x) -> None:
        self.lst.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.lst.pop()
    
    def is_empty(self) -> bool:
        return False if self.lst else True
    

s = Stack()

s.push(1)
s.push(2)


print(s.is_empty())