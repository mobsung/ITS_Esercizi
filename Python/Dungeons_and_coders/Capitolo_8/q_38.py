'''
Nel reticolo delle misure i numeri compaiono ovunque. Implementa `sum_numbers(obj)` in modo **ricorsivo**: se `obj` è un intero o un float, restituiscilo direttamente; se è una lista o una tupla, richiama `sum_numbers` su ciascun elemento e somma i risultati; se è un dizionario, richiama `sum_numbers` su ciascun valore e somma i risultati; se è un altro tipo, restituisci 0. In questo modo tutti i numeri, passo dopo passo, vengono inclusi nel calcolo. Mantieni la firma e fai in modo che superi i test.
'''


def sum_numbers(obj: int | float | list | tuple | dict) -> float:

    result: int | float = 0
    if isinstance(obj, int) or isinstance(obj, float):
        return obj 

    if isinstance(obj, dict):
        for value in obj.values():
            if isinstance(value, int) or isinstance(value, float):
                result += value
            
            if isinstance(value, list) or isinstance(value, dict) or isinstance(value, tuple):
                result += sum_numbers(value)

    if isinstance(obj, list) or isinstance(obj, tuple):
        for depth in obj:
            if isinstance(depth, int) or isinstance(depth, float):
                result += depth

            if isinstance(depth, list) or isinstance(depth, dict) or isinstance(depth, tuple):
                result += sum_numbers(depth)

    return result




print(sum_numbers({'a':{'b':2.5}}))
print(sum_numbers({'x':(1,2,3)}))
# print(sum_numbers(7))
