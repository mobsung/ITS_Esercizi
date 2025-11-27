'''

Un garage fa pagare una tariffa minima di 2.00 $ per parcheggiare fino a tre ore, più 0.50 $ all'ora per ogni ora o parte di essa oltre le tre ore. Il costo massimo per un dato periodo di 24 ore di parcheggio ammonta a 10.00 $. Supponete che nessuna macchina resti parcheggiata per più di 24 ore.
Elaborare un algoritmo che calcoli e stampi i costi del parcheggio per ciascuno dei tre clienti che ieri hanno parcheggiato le loro auto in questo garage.
E' richiesto sapere le ore di parcheggio per ogni cliente.

Una volta elaborato l'algoritmo, scrivere in Python, una funzione calculateCharges che consenta di determinare il costo del parcheggio per ogni cliente.
Mostra, poi, i risultati in forma tabellare.
Il vostro output deve avere il seguente formato:

Car         Hours          Charge
1           1.5            2.00 $
2           4.0            2.50 $
3           24.0           10.00 $
TOTAL       29.5           14.50 $  
'''



# def calculateCharges(ore: float) -> str:

#     euro: float = 0

#     if ore <= 3:
#         euro = 2.0
    
#     else:
#         euro = 2.0
#         for i in range(3, ore):
#             euro += 0.5
#             if i > 17:
#                 break

#     print(f'{euro:<5}$')


def calculateCharges(ore: float) -> str:

    if ore <= 3:
        euro = 2

    elif ore >= 19:
        euro = 10

    else:
        euro = 2 + ((ore - 3) * 0.5)

    return euro



print(f"{'Car':<10}{'Hours':<10}{'Charge':<10}")
print(f"{1:<10}{1.5:<10}{calculateCharges(1.10):<10}")
print(f"{2:<10}{4:<10}{calculateCharges(4):<10}")
print(f"{3:<10}{24:<10}{calculateCharges(24):<10}")
print(f"{'TOTAL':<10}{29.5:<10}{calculateCharges(1.5)+calculateCharges(4)+calculateCharges(24):<5}")