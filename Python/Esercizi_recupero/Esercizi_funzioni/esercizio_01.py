'''
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''


lista: list[tuple[str, str]] = [('a', 'A'), ('b', 'B'), ('c', 'C'), ('c', 'C1')]


def myDict(lista: list[tuple[str, str]]) -> dict[str, str]:
    result_dict: dict[str, str] = {}

    for key, value in lista:
        if key not in result_dict:
            result_dict[key] = str(value)
        else:
            result_dict[key] += str(value)

    return result_dict

print(myDict(lista))
print(dict(lista))
print({key: value for (key, value) in lista})