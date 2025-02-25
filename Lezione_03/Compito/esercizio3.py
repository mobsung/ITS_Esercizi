'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''



stringa:str = input("Digita una stringa!\n>")   #Input richiesto all'utente
reverse_string:str = ""     #Variabile str inizializzata a "" per il il salvataggio della stringa invertita
for index in range(len(stringa), 0, -1): #Algorito per la creazione della stringa invertita
    reverse_string += stringa[index - 1]
print(f"Il contrario della stringa <{stringa}> è <{reverse_string}>")   #Output per l'utente
