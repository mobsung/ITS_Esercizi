'''
Due ricettari si sovrappongono: fondili lasciando prevalere le dosi più aggiornate. Implementa `merge_overwrite(a, b)` creando un nuovo dizionario con i valori di `b` che sovrascrivono `a`. Mantieni la firma e promuovi i test.
'''

def merge_overwrite(a: dict, b: dict) -> dict:
    
    for k in b:
        a[k] = b[k]
        
    return a


print(merge_overwrite({'a': 1, 'b': 2}, {'c': 2, 'a': 3}))