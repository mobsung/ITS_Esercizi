'''
4. CAP e codici
Obiettivo: Lavorare con lunghezze fisse e caratteri misti.

Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).
Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 6 lettere, 2 numeri, 1 lettera, 2 numeri.
'''

import re

# Esercizio 4.1
def is_cap(text:str) -> None:

    print(True if re.fullmatch(r'[0-9]{5}', text) else False)

# expected #True
is_cap("00132")

# expected #False
is_cap("000132")


# Esercizio 4.2
def is_cf(text:str) -> None:

    print(True if re.fullmatch(r'[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}', text) else False)

#expected #True
is_cf("ABCDEF45G67")

#expected #False
is_cf("ABCSDFSDEF45G67")