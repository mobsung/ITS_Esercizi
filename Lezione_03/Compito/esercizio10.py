'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

1 - acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
2 - calcolare e visualizzare la somma di tutti i numeri pari inseriti;
3 - calcolare e visualizzare la media di tutti i numeri dispari inseriti;
4 - determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
5 - se più numeri hanno la stessa frequenza massima, visualizzarli tutti.'''


n:int = int(input("Digita un numero!\n>")) #Inserimento del primo numero richiesto all'utente
somma:int = 0   #Variabile inizializzata a 0 per la somma dei numeri pari
media:float = 0 #Variabile inizializzata a 0 per il calcolo della media dei numeri dispari
contatore:int = 0 #Variabile inizializzata a 0 per il conteggio dei numeri dispari
frequenza:int = 0   #Variabile inizializzata a 0 in qaunto necessaria per la condizione "elif frequenza != number_dict[str(n)]:" che deve verificarsi sempre
number_dict:dict[str, int] = {} #Inizializzazione dizionario che conterrà i valori singoli e le volte che si ripetono
numeri_frequenti:list[int] = [] #Inizializzazione lista che conterrà i valori che si ripetono di più ed il numero di ripetizioni
final_list:list[int] = []   #Inizializzazione lista che conterrà solo i valori senza numero di ripetizioni
while n != 0:   #Algoritmo per il calcolo di somma, media e conteggio ripetizioni
    if str(n) not in number_dict:
        number_dict[str(n)] = 1
    elif frequenza != number_dict[str(n)]:
         frequenza = number_dict[str(n)] 
         number_dict[str(n)] = frequenza + 1
         frequenza = 0
    if n % 2 == 0:
        somma += n
        n:int = int(input("Digita 0 per terminare altrimenti digita un'altro numero per continuare!\n>"))
    else:
        media += n
        contatore += 1
        n:int = int(input("Digita 0 per terminare altrimenti digita un'altro numero per continuare!\n>"))

for key, value in number_dict.items():  #Algorito per estrazione valori che si ripetono di più con il numero di ripetizioni
    if numeri_frequenti[:] ==  []:
        numeri_frequenti.append((key, value))
    elif numeri_frequenti[0][1] < number_dict[key]:
        del numeri_frequenti[:]
        numeri_frequenti.append((key, value))
    elif numeri_frequenti[0][1] == number_dict[key]:
        numeri_frequenti.append((key, value))

for i in range (len(numeri_frequenti)): #Algoritmo per l'estrazione dei valori senza numero ripetizioni
    final_list.append(numeri_frequenti[i][0])

print(f"La somma dei numeri è: {somma}")
print(f"La media dei numeri dispari è: {media / contatore:.4f}")
print(f"I numeri che si ripetono di più sono i seguenti: {', '.join(final_list)} con una frequenza di {numeri_frequenti[0][1]} volte")


