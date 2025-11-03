'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

For example:
Test 	Result

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))

{'a': [1, 3], 'b': [2]}

print(lista_a_dizionario([]))
{}
'''


def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo code

    result_dict: dict[str:list[int]] = {}

    for tup in tuples:
        if tup[0] not in result_dict.keys():
            result_dict[tup[0]] = [tup[1]]
        else:
            result_dict[tup[0]].append(tup[1])

    return result_dict

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))