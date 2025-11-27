'''
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

print(somma_elementi([1,1,1],[1,1,1])) -> [2, 2, 2]
'''



def somma_elementi(x: list[int], y: list[int]) -> list[int]:

    sum_list:list[int] = []

    for i in range(len(x)):

        sum_list.append(x[i] + y[i])

    return sum_list


print(somma_elementi([1,1,1],[1,1,1]))