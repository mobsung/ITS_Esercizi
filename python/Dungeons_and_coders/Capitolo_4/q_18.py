'''
Nel reattore il primo reagente attiva il successivo: realizza `compose(f, g)` perché la funzione restituita calcoli prima `g(x)` e poi `f(...)`. Mantieni la firma e titola i test alla perfezione.
'''

def compose(f, g):
    
    def first_step(x):
        return f(g(x))

    return first_step