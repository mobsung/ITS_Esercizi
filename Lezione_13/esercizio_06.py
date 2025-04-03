'''Esercizio 6.

Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.
'''


def recursivePi(n:int):

    if n < 0:
        print("Numero non valido")
    elif n == 0:
        return 2
    else:
        return (n + 2) * recursivePi(n - 1)


print(recursivePi(7))