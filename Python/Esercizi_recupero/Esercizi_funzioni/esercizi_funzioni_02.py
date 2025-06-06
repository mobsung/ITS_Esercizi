'''
2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''


def multiply(lista: list[int], threshold: int) -> int:

    result: int = 1

    for num in lista:
        if num < threshold:
            result *= num
    
    return 0 if len(lista) == 0 else result

print(multiply([1, 2, 3, 4, 5, 6, 6], 5))