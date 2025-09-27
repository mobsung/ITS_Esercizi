'''
Sigilla una dose costante in un flacone: ogni goccia aggiunge sempre la stessa quantità. Implementa `curry_add(n)` perché ritorni una funzione che somma `n` al valore ricevuto. Mantieni la firma e promuovi i test.
'''


def curry_add(n):
    
    def add(x):
        return n + x
    
    return add