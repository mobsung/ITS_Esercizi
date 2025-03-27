'''In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato #1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.'''

import random


# funzione per la definizione delle azioni della lepre
def azioni_lepre(posizione_lepre:int = 0, stamina_lepre:int = 100) -> int:

    azione:int = random.randint(1, 10) #generazione numero random da 1 a 10 per coprire il 100% di possibilità

# match case per la verifica casistica con le eventuali mosse da parte della Lepre 
    match azione:
        case azione if 1 <= azione <= 2:
            spostamento = 0
            stamina_lepre = stamina_lepre + 10 if stamina_lepre <= 90 else 100
            print("--->La Lepre si riposa e recupera 10 Stamina")
        case azione if 3 <= azione <= 4 and stamina_lepre >= 15:
            stamina_lepre -= 15
            spostamento = 9
            print(f'--->La Lepre fa un grande balzo - Si sposta di {spostamento} caselle avanti e consuma 15 Stamina!')
        case azione if azione == 5 and stamina_lepre >= 20:
            stamina_lepre -= 20
            spostamento = -12
            print(f'--->La Lepre fa una grande scivolata - Arretra di {abs(spostamento)} caselle e consuma 20 Stamina!')
        case azione if 6 <= azione <= 8 and stamina_lepre >= 5:
            stamina_lepre -= 5
            spostamento = 1
            print(f'--->La Lepre fa un piccolo balzo - Si sposta di una casella e consuma 5 Stamina!')
        case azione if 9 <= azione <= 10 and stamina_lepre >= 8:
            stamina_lepre -= 8
            spostamento = -2
            print(f'--->La Lepre fa una piccola scivolata - Aretra di {abs(spostamento)} caselle e consuma 8 Stamina!')
        case _:
            print(f'La Lepre rimane ferma in quanto non ha sufficiente Stamina!')
            spostamento = 0
            pass

    posizione_lepre += spostamento
    if posizione_lepre < 0: # verifica se la posizione è minore di 0, se lo è viene impostata a 0
        print("--->La posizione non può essere inferiore a 0")
        posizione_lepre = 0

    print(f'--->Posizione Lepre - {posizione_lepre} | Stamina Lepre - {stamina_lepre}!')
    return posizione_lepre, stamina_lepre # il return della parametro posizione_lepre e stamina_lepre

# funzione per la definizione delle azioni della tartaruga
def azioni_tartaruga(posizione_tartaruga:int = 0, stamina_tartaruga:int = 100) -> int:

    azione:int = random.randint(1, 10) #generazione numero random da 1 a 10 per coprire il 100% di possibilità

# match case per la verifica casistica con le eventuali mosse da parte della Tartaruga 
    match azione:
        case azione if azione <= 5 and stamina_tartaruga >= 5:
            stamina_tartaruga -= 5
            spostamento = 3
            print(f"--->La Tartaruga fa un passo veloce - Si sposta di {spostamento} caselle e consuma 5 Stamina!")
        case azione if 6 <= azione <= 7 and stamina_tartaruga >= 10:
            stamina_tartaruga -= 10
            spostamento = -6
            print(f'--->La Tartaruga fa una scivolata - Arretra di {abs(spostamento)} caselle e consuma 10 Stamina!')
        case azione if azione >= 8 and stamina_tartaruga >= 3:
            stamina_tartaruga -= 3
            spostamento = 1
            print(f'--->La Tartaruga fa un passo lento - Si sposta di una casella e consuma 3 Stamina!')
        case _:
            print(f'La Tartaruga rigenera 10 Stamina!')
            spostamento = 0
            stamina_tartaruga += 10 if stamina_tartaruga <= 90 else 100 
            pass

    posizione_tartaruga += spostamento
    if posizione_tartaruga < 0: # verifica se la posizione è minore di 0, se lo è viene impostata a 0
        print("--->La posizione non può essere inferiore a 0")
        posizione_tartaruga = 0

    print(f'--->Posizione Tartaruga - {posizione_tartaruga} | Stamina Tartaruga - {stamina_tartaruga}!')
    return posizione_tartaruga, stamina_tartaruga # il return della parametro posizione_tartaruga e stamina_tartaruga

# funzione per la creazione del percorso e la simulazione della gara
def gara(posizione_tartaruga:int = 0, posizione_lepre:int = 0, stamina_lepre = 100, stamina_tartaruga = 100, range_caselle:int = 70):
    
    tick: int = 0 # inizializzazione variabile a 0 per il conteggio delle mosse
# inizializzazione variabile pioggia a True e variabile sole a False in quanto devono alternarsi
    pioggia:bool = True 
    sole:bool = False 

    ostacoli: dict[int, int] = {15: -3, 30: -5, 45: -7} # inizializzazione dizionario ostacoli
    bonus: dict[int, int] = {10: 5, 25: 3, 50: 10} # inizializzazione dizionario bonus

    print("'BANG !!!!! AND THEY'RE OFF !!!!!'\n")
    
# ciclo while che si verifica finche una o entrambe le posizioni superano 69
    while posizione_tartaruga <= 70 and posizione_lepre <= 70: 

        if tick % 10 == 0: # condizione che inverte il valore delle variabili pioggia e sole ogni 10 tick
            pioggia = not pioggia
            sole = not sole

        percorso: list[int] = [] # inizializzazione lista vuota da riempire con le caselle del percorso

        for i in range(range_caselle - 1): # ciclo for che genera una lista piena di caselle vuote ogni tick
            percorso.append("_")
            
        if tick == 0: # condizione che si verifica una sola volta e posiziona la Lepre e la Tartaruga nella prima casella
            posizione_lepre = -1
            posizione_tartaruga = -1
            percorso.insert(posizione_lepre, "OUCH!")

        elif pioggia == True:
            print("--->Piove!")
            print(f'--->Mossa n°{tick}!')
            posizione_lepre, stamina_lepre = azioni_lepre(posizione_lepre - 2, stamina_lepre)
            posizione_tartaruga, stamina_tartaruga = azioni_tartaruga(posizione_tartaruga - 1, stamina_tartaruga)

            posizione_lepre = posizione_lepre + ostacoli[posizione_lepre] if posizione_lepre in ostacoli else posizione_lepre
            posizione_tartaruga = posizione_tartaruga + ostacoli[posizione_tartaruga] if posizione_tartaruga in ostacoli else posizione_tartaruga

            posizione_lepre = posizione_lepre + bonus[posizione_lepre] if posizione_lepre in bonus else posizione_lepre
            posizione_tartaruga = posizione_tartaruga + bonus[posizione_tartaruga] if posizione_tartaruga in bonus else posizione_tartaruga

            if posizione_lepre != posizione_tartaruga:
                percorso.insert(posizione_tartaruga - 1, "T") if posizione_tartaruga > 0 else percorso.insert(posizione_tartaruga, "T")
                percorso.insert(posizione_lepre - 1, "H") if posizione_lepre > 0 else percorso.insert(posizione_lepre, "H")

            else:
                percorso.insert(posizione_lepre, "OUCH!")
        else:
            print("--->Tempo soleggiato!")
            print(f'--->Mossa n°{tick}!')
            posizione_lepre, stamina_lepre = azioni_lepre(posizione_lepre, stamina_lepre)
            posizione_tartaruga, stamina_tartaruga = azioni_tartaruga(posizione_tartaruga, stamina_tartaruga)

            posizione_lepre = posizione_lepre + ostacoli[posizione_lepre] if posizione_lepre in ostacoli else posizione_lepre
            posizione_tartaruga = posizione_tartaruga + ostacoli[posizione_tartaruga] if posizione_tartaruga in ostacoli else posizione_tartaruga

            posizione_lepre = posizione_lepre + bonus[posizione_lepre] if posizione_lepre in bonus else posizione_lepre
            posizione_tartaruga = posizione_tartaruga + bonus[posizione_tartaruga] if posizione_tartaruga in bonus else posizione_tartaruga


            if posizione_lepre != posizione_tartaruga:
                percorso.insert(posizione_tartaruga - 1, "T") if posizione_tartaruga > 0 else percorso.insert(posizione_tartaruga, "T")
                percorso.insert(posizione_lepre - 1, "H") if posizione_lepre > 0 else percorso.insert(posizione_lepre, "H")
                
            else:
                percorso.insert(posizione_lepre, "OUCH!")
        print(f'{"".join(percorso)}\n') 

        tick += 1

    if posizione_tartaruga >=70:
        print("TORTOISE WINS! || VAY!!!")
    elif posizione_tartaruga >= 70 and posizione_lepre >= 70:
        print("IT'S A TIE.")
    else:
        print("HARE WINS || YUCH!!!")



gara()