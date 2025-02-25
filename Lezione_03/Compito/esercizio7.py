'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''



a:list[int] = [4, 6, 12, 47, 5, 17, 35]  #Lista a con 7 elementi
b:list[int] = [2, 43, 73, 11, 9, 7, 14]  #Lista b con 7 elementi
c:list[int] = []    #Inizializazione lista c vuota
n:int = len(a) - 1  #Inizializzazione variabile n = alla lunghezza della lista - 1 in quanto l'ultimo elemento della lista ha valore 6
for i in range(n + 1):  #Algoritmo per la modifica della lista c con la somma incrociata degli elementi delle liste a e b
    c.append(a[i] + b[n - i])
print(f"Lista a: {a}")              
print(f"Lista b: {b}")              
print(f"Lista c: {c}")  #Output per l'utente
