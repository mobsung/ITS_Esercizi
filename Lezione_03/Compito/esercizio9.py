'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

- progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''


pi_2f:bool = False #variabile inizializzata a False per non far verificare la condizione ogni volta che si verifica 
pi_3f:bool = False
pi_4f:bool = False
pi_5f:bool = False
pi:float = 4
iterazioni:int = 0 #Variabile inizializzata a 0 per il conteggio del numero di iteraizoni
for i in range (3, 1000000, 4): #Algorto per il calcolo e la verifa del valore di π
    pi = pi - 4/i + 4/(i + 2)
    iterazioni += 1 
    if not pi_2f and float(f"{pi:.2f}") == 3.14:
        pi_2f = True    #Aggiornamento della variabile booleana a True per interrompere la verifica della condizione dopo la prima volta che si è verificata
        print(f"π raggiunge il valore: {pi:.2f} alla {iterazioni}° iterazione")
    if not pi_3f and float(f"{pi:.3f}") - 0.001 == 3.141:   #Condizione aggiustata per correggere l'arrotondamento per eccesso tramite la funzione ":.f"
        pi_3f = True
        print(f"π raggiunge il valore: {pi - 0.001:.3f} alla {iterazioni}° iterazione")
    if not pi_4f and float(f"{pi:.4f}") - 0.0006 == 3.1415: #Condizione aggiustata per correggere l'arrotondamento per eccesso tramite la funzione ":.f"
        pi_4f = True
        print(f"π raggiunge il valore: {pi - 0.0006:.4f} alla {iterazioni}° iterazione")
    if not pi_5f and float(f"{pi:.5f}") == 3.14159:
        pi_5f = True
        print(f"π raggiunge il valore: {pi:.5f} alla {iterazioni}° iterazione")