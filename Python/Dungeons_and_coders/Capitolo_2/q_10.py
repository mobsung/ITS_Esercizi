'''
Nelle linee di distillazione annidate segui la mappa passo dopo passo, altrimenti ricorri alla dose di sicurezza. Implementa `deep_get(d, path, default)`, avanzando tra dizionari e liste `d` seguendo `path`; restituisci il passo ma, se manca, ritorna `default`. Mantieni la firma e supera i test.
'''

def deep_get(d: dict | list, path: list, default=None):

    if len(d) == 0:
        return default

    for step in path:
        if type(step) == list and len(d) < step:
            return default
        
        if type(step) == dict and step not in d:
            return default
        
        else:
            d = d[step]
        
    return d
