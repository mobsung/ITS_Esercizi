'''
Se il solvente è nullo, la reazione non parte: usa il tampone. Con `divide_safe(a, b, default=None)` torna `a/b` se `b` ≠ `0`, altrimenti `default`. Mantieni la firma e promuovi i test.
'''


def divide_safe(a, b, default=None):
    
    return default if b == 0 else a / b