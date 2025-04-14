'''
1. Riconoscere numeri
Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).
'''

import re

# positive test # re.fullmatch(r'\d+', text)
def isPositive(text:str) -> None:

    print(True if re.fullmatch(r'\d+', text) else False)

# "123" expected True
isPositive("123")

# "98765" expected True
isPositive("98765")

# "-123" expected False
isPositive("-123")

# 1.23 expecter False
isPositive("1.23")


# negative test # re.fullmatch(r'-\d+', text)
def isNegative(text:str) -> None:

    print(True if re.fullmatch(r'-\d+', text) else False)

# "-123" expected True
isNegative("-123")

# "123" expected False
isNegative("123")

# "-1.23" espected false
isNegative("-1.23")
