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
def azioni_lepre(posizione_lepre:int = 0) -> int:

    azione:int = random.randint(1, 10)
    spostamento: int = 0

    match azione:
        case 1 | 2:
            spostamento = 0
            print("La Lepre si riposa!")
        case 3 | 4:
            spostamento = 9
            print(f'La Lepre fa un grande balzo e si sposta di {spostamento} caselle avanti!')
        case 5:
            spostamento = -12
            print(f'La Lepre fa una grande scivolata e arretra di {spostamento // 1} caselle!')
        case 6 | 7 | 8:
            spostamento = 1
            print(f'La Lepre fa un piccolo balzo e si sposta di una casella!')
        case 9 | 10:
            spostamento = -2
            print(f'La Lepre fa una piccola scivolata e aretra di {spostamento // 1} caselle!')
        case _:
            pass

    posizione_lepre += spostamento
    if posizione_lepre < 0:
        posizione_lepre = 0

    return posizione_lepre

# funzione per la definizione delle azioni della tartaruga
def azioni_tartaruga(posizione_tartaruga:int = 0) -> int:

    azione:int = random.randint(1, 10)
    spostamento: int = 0

    match azione:
        case azione if azione < 6:
            spostamento = 3
            print(f"La Tartaruga fa un passo veloce e si sposta di {spostamento} caselle!")
        case 6 | 7:
            spostamento = -6
            print(f'La Tartaruga fa una scivolata e arretra di {spostamento // 1} caselle!')
        case azione if azione > 7:
            spostamento = 1
            print(f'La Tartaruga fa un passo lento e si sposta di {1} casella!')
        case _:
            pass

    posizione_tartaruga += spostamento
    if posizione_tartaruga < 0:
        posizione_tartaruga = 0
    
    return posizione_tartaruga

# funzione per la creazione del percorso e la simulazione della gara
def gara(posizione_tartaruga:int = 0, posizione_lepre:int = 0, range_caselle:int = 70):
    
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'\n")

    while posizione_tartaruga <= 70 and posizione_lepre <= 70:
        percorso: list[int] = []
        for i in range(range_caselle + 1):
            percorso.insert(i, "_")

        posizione_lepre = azioni_lepre(posizione_lepre)
        posizione_tartaruga = azioni_tartaruga(posizione_tartaruga)
            
        if posizione_lepre != posizione_tartaruga:
            percorso.insert(posizione_tartaruga, "T")
            percorso.insert(posizione_lepre, "H")
        else:
            percorso.insert(posizione_lepre, "OUCH!")
        print(f'{percorso}\n') 

    if posizione_tartaruga >=70:
        print("TORTOISE WINS! || VAY!!!")
    elif posizione_tartaruga >= 70 and posizione_lepre >= 70:
        print("IT'S A TIE.")
    else:
        print("HARE WINS || YUCH!!!")


gara()

    

