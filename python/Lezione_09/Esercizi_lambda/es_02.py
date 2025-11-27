'''
Esercizio 2 - Somma di due numeri
Crea una funzione lambda che accetti due numeri e restituisca la loro somma.
'''

from typing import Callable

sum_two:Callable[[int], int] = lambda x, y: x + y


# TEST x = 2, y = 3 EXPECTED 5
print(sum_two(2, 3))