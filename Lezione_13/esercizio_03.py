'''Esercizio 3.

Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
'''


def recursiveFactorial(n:int) -> int:

    if n < 0:
        print("Error! Inserted number is negative!")
        return None
    # if n = 0 recursive process must be stopped
    elif n < 1:
        return 1
    # if n is positive, compute recursive moltiplication
    else:
        return int(n * recursiveFactorial(n - 1))

print(recursiveFactorial(20))




# 3 * (3 - 1) * (3 - 2)