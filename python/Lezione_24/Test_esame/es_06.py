'''

Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

For example:
Test 	Result

print(classifica_numeri([1, 2, 3, 4, 5, 6])) 

	

{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))

	

{'pari': [], 'dispari': []}
'''

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice
    result_dict: dict[str:list[int]] = {'pari': [], 'dispari': []}

    for num in lista:
        if num % 2 == 0:
            result_dict['pari'].append(num)
        else:
            result_dict['dispari'].append(num)
    return result_dict