'''
Esercizio 1 - Sintassi
Scrivi una funzione lambda che prenda un numero intero e ritorni il suo quadrato.

Esempio atteso:

quadrato = lambda x: ...
'''

from typing import Callable

quadrato:Callable[[int], int] = lambda x: x ** 2

# TEST x = 4 Expected 16
print(quadrato(4))

# TEST x = 16 Expected 256
print(quadrato(16))