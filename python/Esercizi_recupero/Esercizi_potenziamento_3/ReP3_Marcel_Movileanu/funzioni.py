'''
All'interno del file ReP3_inizialeNome_Cognome (fuori dalla classi) definire le seguenti funzioni:

    pariUguali(a: list[int], b: list[int]). Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.

Ogni elementi della lista c deve essere uguale a:
- 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
- 0 altrimenti

    combattimento(a: Alieno, m: Mostro). Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro. Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un Mostro, il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice. Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro. Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro. Altrimenti, il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria, altrimenti viene stampato il gemito della sconfitta.


    proclamaVincitore(c: Creatura). Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e , mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.
'''


from creatura import Creatura
from mostro import Mostro
from alieno import Alieno


def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []
    for i in range(15):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c


def combattimento(a: Alieno, m: Mostro) -> Mostro | Alieno | None:
    if isinstance(a, Alieno) and isinstance(m, Mostro):
        if pariUguali(a.munizioni(), m.assalto()).count(1) >= 4:
            print(f'{m.urlo_vittoria()}\n'*3)
            return(m)
        else:
            print(m.gemito_scofitta())
            return(a)
    else:
        print('Oggetti non validi')
        return None
    

def proclamaVincitore(c: Creatura) -> None:
    larghezza_totale = len(str(c)) + 10
    bordo = '*' * larghezza_totale
    riga_vuota = '*' + ' ' * (larghezza_totale - 2) + '*'
    
    # Riga con il nome centrato
    contenuto = str(c)
    spazi = larghezza_totale - 2 - len(contenuto)
    padding_sinistra = spazi // 2
    padding_destra = spazi - padding_sinistra
    riga_nome = '*' + ' ' * padding_sinistra + contenuto + ' ' * padding_destra + '*'
    
    # Stampa il tutto
    print(f"{'Gli alieni hanno vinto!' if isinstance(c, Alieno) else 'I mostri hanno vinto!'}")
    print(bordo)
    print(riga_vuota)
    print(riga_nome)
    print(riga_vuota)
    print(bordo)