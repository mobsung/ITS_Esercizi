'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

1 - Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
2 - Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

number_list:list[float] = []    #Inizializzazione lista che conterrà i valori inseriti in input dall'utente
counter:int = 0 #Variabile inizializzata a 0 che viente aumentata di 1 ogni volta che viente inserito un numero intero
media:float = 0 #Variabile inizializzata a 0 per il calcolo della media dei valori interi inseriti dall'utente
number:int = float(input("Digita un numero\n>"))
while True: #Ciclo che si ripete finche il numero inserito è maggiore di 0
    if number >= 0: #Algorito per il salvataggio di numeri in una lista e per il calcolo della media dei numeri interi
        if number.is_integer():
            media += number
            counter += 1
        number_list.append(number)
        number:int = float(input("Digita un'altro numero\n>"))
    else: #Condizione che termina l'algorito quanto viene digitato il numero 0
        break
print(f"La media dei numeri interi è: {media / counter}")   #Output per l'utente
number_list.sort()  #Funzione per il sorting della lista in ordine crescente
print(f"Il numero più grande è: {number_list[len(number_list) - 1]}") #Output numero maggiore equivalente all'ultimo elemento della lista 
print(f"Il numero più piccolo è: {number_list[0]}") ##Output numero minore equivalente al primo elemento della lista


