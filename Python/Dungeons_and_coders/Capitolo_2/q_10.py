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


print(deep_get({'a':{'b':[10,20]}},['a','b',1]))
print(deep_get({},['x'],7))
print(deep_get({'k':[{'z':5}]},['k',0,'z'],0))
print(deep_get([{'a':1}],[0,'a'],None))
print(deep_get({'a':{'b':{'c':9}}},['a','b','c']))
print(deep_get({'a':[1,2]},['a',1]))