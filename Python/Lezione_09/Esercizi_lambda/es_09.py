'''
Scrivi una funzione moltiplicatore(n) che ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20
'''


def moltiplicatore(n: int):
    return lambda x: x * n

per_due = moltiplicatore(2)
print(per_due(10))