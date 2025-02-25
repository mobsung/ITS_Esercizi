'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.'''


stringa:str = input("Digita una stringa!\n>") #Input richiesto all'utente
numero_spazi:int = 0    #Variabile inizializzata a 0 per il conteggio degli spazi vuoti
for elemento in stringa:    #Algoritmo per la verica degli spazi vuoti
    if elemento == " ":
        numero_spazi += 1
print(f"Il numero di spazi nella striga inserita equivale a: {numero_spazi} spazi!")    #Output per l'utente