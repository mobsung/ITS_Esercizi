'''
Al banco di distillazione serve un registro impeccabile. Fai parlare la procedura: implementa `Counter` con base **0**, metodo `inc()` che incrementa di **1** e `value()` che restituisce il numero di prove completate. Mantieni la firma data e fai superare tutti i test automatici.
'''


class Counter:
    
    def __init__(self) -> None:
        self.val = 0

    def inc(self) -> None:
        self.val += 1

    def value(self) -> int:
        return self.val
    
c = Counter()

c.inc()
c.inc()
c.inc()

print(c.value())