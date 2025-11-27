'''
Esercizio 5 - Funzione lambda con if
Crea una funzione lambda che prenda un numero e ritorni "pari" se è divisibile per 2, altrimenti "dispari".
'''

from typing import Callable

pari_dispari: Callable[[int], str] = lambda x: 'pari' if x % 2 == 0 else 'dispari'


# TEST x = 4 Expected 'pari'
print(pari_dispari(4))

# TEST x = 5 Expected 'dispari'
print(pari_dispari(5))