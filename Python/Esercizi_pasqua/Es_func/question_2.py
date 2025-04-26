'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.
For example:

Test	                                            Result
print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))  ->  {1: 'a', 2: 'b', 3: 'c'}

print(inverti_mappa({}))                        ->  {}
'''


def inverti_mappa(dizionario: dict[str:int]) -> dict[int, str]:

    inverted_dict: dict[str:int] = {}

    for key, value in dizionario.items():

        if value not in inverted_dict.keys():
            inverted_dict[value] = key

    return inverted_dict


if __name__ == "__main__":
    print(inverti_mappa({'a': 1, 'b': 2, 'c': 3, "d": 3}))
    print(inverti_mappa({}))