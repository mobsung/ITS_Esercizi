'''
La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.
Trova l'errore e correggi il codice affinché soddisfi i casi di test.
For example:

Test	                                        Result
print(calculate_average([1, 2, 3, 4, 5])) ->    3.0

print(calculate_average([]))              ->    0

'''


def calculate_average(numbers: list[int]) -> float:
    
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return 0
    

if __name__ == "__main__":
    print(calculate_average([1, 2, 3, 4, 5]))

    print(calculate_average([2]))