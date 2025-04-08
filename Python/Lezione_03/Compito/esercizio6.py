'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''



n1:int = int(input("Digita un numero!\n>")) #Inserimento del primo numero richiesto all'utente 
n2:int = int(input("Digita un'altro numero!\n>"))   #Inserimento del secondo numero richiesto all'utente 
prod:int = 1    #Inizializzazione variabile prodotto a 1 
if n1 < n2: #Condizione per il caso n1 < n2
    for numero in range(n1, n2 + 1, 1):
        prod *= numero
else:   #Condizione per il caso n1 < n2
    for numero in range(n1, n2 - 1, -1):
        prod *= numero
print(f"Il prodotto dei numeri compresi tra {n1} e {n2} è: {prod}") #Output per l'utente