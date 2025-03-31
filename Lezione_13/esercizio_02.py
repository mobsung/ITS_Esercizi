'''Esercizio 2.
Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.
'''


def compoundInterest(t:int, m:float = 100) -> None:

    if t == 0:
        print(f'The total money is {m:.2f}')
    
    elif t > 0:
        m *= 1.005
        compoundInterest(t - 1, m)


compoundInterest(500)


