'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
For example:

Test	                                             Result
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))  -> [1, 3, 4]

print(rimuovi_elementi([], {2: 1}))               -> []
'''


def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    result_lista: list[int] = lista.copy()

    for num in lista:
        if num in da_rimuovere.keys():
            result_lista.remove(num)

            if da_rimuovere[num] > 1:
                da_rimuovere[num] -= 1
            else:
                da_rimuovere.pop(num)
    
    return result_lista

if __name__ == "__main__":
    print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2, 3: 2}))

    print(rimuovi_elementi([], {2: 1}))