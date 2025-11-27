'''

Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato il diagramma, appena consentitovi dal docente, scrivere una funzione ricorsiva in Python, chiamata printListBackward che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver date le seguneti liste, stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva printListBackward.

    lista1: 1, 2, 3, 4, 5

    lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"

'''

from typing import Any

def printListBackward(lista: list[Any]) -> list[Any]:
    if init == True:
        result_list: list[Any] = []
        init = False

    result_list.append(lista[-1])
    lista.remove(lista[-1])

    if len(lista) == 0:
        print(result_list)

    else:
        return printListBackward(lista)
    

printListBackward([1, 2, 3, 4, 5])