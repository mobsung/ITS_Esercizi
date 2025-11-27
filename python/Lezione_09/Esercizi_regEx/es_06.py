'''
. Codici personalizzati

Obiettivo: Unire lettere, numeri e caratteri speciali.

    Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.
    Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere lettere maiuscole e      
    numeri (es. AB12CD34).

'''

import re

# Esercizio 6.1
def isId(text:str) -> None:

    print(True if re.fullmatch(r'[A-Z]{4}-\d{4}-[A-Z]{2}', text) else False)

# expected True
isId("PROD-1234-XY")

# expected False
isId("PRD-12234-XXY")


def isIdAlp(text:str) -> None:

    print(True if re.fullmatch(r'[A-Z0-9]{8}', text) else False)


# expexcted True
isIdAlp("AB12CD34")

# expexcted False
isIdAlp("AB12AsCD34")
