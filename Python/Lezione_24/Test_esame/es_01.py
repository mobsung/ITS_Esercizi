'''

Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

For example:
Test 	Result

print(sum_above_threshold([15, 5, 25], 20))

	

25
'''

def sum_above_threshold(numbers: list[int], threshold:int) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    
    tot: int = 0

    for num in numbers:
        if num > threshold:
            tot += num

    return tot


print(sum_above_threshold([1, 10, 20, 30], 10))