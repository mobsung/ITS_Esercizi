'''
Unisci due analisi parziali: con `merge_struct(a, b)` produci un dizionario che copia `a` e aggiorna coi campi di `b` in conflitto. Mantieni la firma e promuovi i test.
'''


def merge_struct(a: dict, b: dict) -> dict:
    
    for key, value in b.items():
        a[key] = value
    
    return a