'''
5. Riconoscere date
Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.
'''

import re

# Esercizio 5.1
def is_date(text:str) -> None:

    print(True if re.fullmatch(r'\d{2}/\d{2}/\d{4}', text) else False)

is_date("09/04/2025")


# Esercizio 5.2
def is_dateEx(text:str) -> None:

    print(True if re.fullmatch(r'\d{2}[/-]\d{2}[/-]\d{4}', text) else False)

is_dateEx("09-04-2025")