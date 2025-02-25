'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
******* '''



number_list:list[int] = []   #Inizializazione lista number_list che conterrà i valuti interi inseriti in input
output_list:list[str] = []   #Inizializazione lista output_list che conterrà il numero di "*" 
n:int = int(input("Digita un numero compreso tra 1 e 30\n>"))   #Primo input richiesto all'utente
while len(number_list) < 5: #Algoritmo per l'inserimento dei successivi 4 numeri richiesti al cliente 
    if n >= 1 and n <= 30:
        number_list.append(n)
        if len(number_list) < 5:
            n:int = int(input("Digita un'altro numero compreso tra 1 e 30\n>"))
    else: 
        n:int = int(input("Numero insererito non valido, digita un numero compreso tra 1 e 30\n>"))
print("Sei arrivato a 5 numeri!")
for elemento in number_list:    #Algoritmo per la stampa dei "*" 
    for i in range(elemento):
        output_list += "*"
    print(f"{''.join(output_list)}")
    del output_list[:]
        

        


    
     
