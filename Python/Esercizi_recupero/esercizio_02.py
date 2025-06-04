'''
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
'''


def divideList(lista:list[int]) -> dict[str, int]:

    result_dict: dict[str, int] = {'positivi': [], 'negativi': []}

    for num in lista:

        if num >=  0:
            result_dict['positivi'].append(num)
        else:
            result_dict['negativi'].append(num)

    return result_dict

print(divideList([1, 2, 3, 4, -5, 6, -4, 5]))