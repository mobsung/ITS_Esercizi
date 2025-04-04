'''
Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:

    tutti i numeri pari vengano prima di tutti i numeri dispari;

    l’ordine relativo tra pari e dispari va mantenuto;

    l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

    rint(even_odd_pattern([3, 6, 1, 8, 4, 7])) -> [6, 8, 4, 3, 1, 7]

'''

def even_odd_pattern(numbers:list[int]) -> list[int]:

    odd_list:list[int] = []
    even_list:list[int] = []

    for char in numbers:
        if char % 2 == 0:
            odd_list.append(char)
        else:
            even_list.append(char)

    return odd_list + even_list
