'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

- Acquisisca in input un valore N (numero di euro disponibili).
- Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
- Mostri quanti buoni sconto avanzano al termine dell'acquisto.

Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.

Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''




euro_disponibili:int = int(input("Quanto soldi hai a disposizione?\n>"))    #Importo diponibile inserito dall'utente
barrette_extra:int = 0  #Variabile che conterà il numero extra di barrette
for barretta in range(5, euro_disponibili, 6): #Calcolo del numero di barrette extra
    barrette_extra += 1
buoni_extra:int = euro_disponibili % 6 #Formula per il calcolo dei buoni inutilizzati utilizzando l'operatore aitmetico "modulo"
print(f"Con {euro_disponibili}$ puoi acquistare <{euro_disponibili + barrette_extra}> barrette e ti rimangono <{buoni_extra}> buoni inutilizzati!") #Output per l'utente