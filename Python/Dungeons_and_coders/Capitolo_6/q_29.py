'''
Contieni la temperatura del crogiolo tra soglia bassa e alta. Implementa `clamp(x, lo, hi)` restituendo il valore limitato a `[lo, hi]`. Mantieni la firma e titola i test.
'''

def clamp(x: float, lo: float, hi: float) -> float:
    
    if lo <= x <= hi:
        return x
    
    elif x < lo:
        return lo
    
    else:
        return hi