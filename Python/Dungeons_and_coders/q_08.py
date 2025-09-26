'''
Per evitare errori, inverti gli indici della tabella: ogni valore rimandi all'essenza originaria. Usa `invert_unique(d)` assumendo valori univoci. Mantieni la firma e passa i test.
'''

def invert_unique(d: dict) -> dict:
    
    new_d: dict = {}

    for key, value in d.items():
        new_d[value] = key

    return new_d
