'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''


parola:str = input("Digita una parola!\n>") #Input richiesto all'utente
while parola != "fine": #Ciclo che si verifica finche la parola inserita è diversa da "fine"
        if parola[0] == parola[len(parola) - 1]:    #Condizione per la verifica dell'uguaglianza tra il primo è l'ultimo carattere
            print(f"La prima e l'ultima lettera della parola {parola} sono uguali!")
            parola:str = input("Digita un'altra parola!\n>")
        else:
            print(f"La prima e l'ultima lettera della parola {parola} sono diverse!")
            parola:str = input("Digita un'altra parola!\n>")    #Output per l'utente

