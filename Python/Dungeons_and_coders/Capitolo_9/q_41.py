'''
Nella camera delle soluzioni turbolente, certi campioni danno misura, altri svaniscono. Distilla con `to_int(x, default=0)`: prova `int(x)` e quando l'estrazione fallisce (`ValueError`/`TypeError`) riporta `default`. Accetta stringhe numeriche e numeri in virgola (`3.2 → 3`). Mantieni la firma e promuovi i test.
'''

def to_int(x, default=0):
    try:
        return int(x)
    except:
        return default