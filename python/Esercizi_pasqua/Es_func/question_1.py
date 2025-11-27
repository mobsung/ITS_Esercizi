'''
Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
For example:

Test	                                             Result
print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))  -> [6, 12, 18]

print(filtra_moltiplica([], 3))                  -> []

'''


def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:

    result_list: list[int] = []

    for number in lista_numeri:
          
        if number % 2 == 0:
            result_list.append(number * fattore)

    return result_list


if __name__ == "__main__":
    print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))
    print(filtra_moltiplica([], 3))