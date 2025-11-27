'''
Nel banco di separazione, trattieni solo i costituenti indicati. Con `pick(d, keys)` crea un nuovo dizionario con le chiavi richieste presenti in `d`, senza alterare `d`. Mantieni la firma e titola i test.
'''


def pick(obj: dict, keys: list[str]) -> dict:
    
    result_dict: dict = {}

    for k in keys:
        if obj.get(k):
            result_dict[k] = obj[k]


    return result_dict