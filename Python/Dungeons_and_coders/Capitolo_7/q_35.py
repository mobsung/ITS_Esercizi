'''
Analizza il front-run del segnale: `head(lines, n)` deve produrre una lista con le prime `n` righe (tutte se `n` eccede). L’originale non si altera. Mantieni la firma e promuovi i test.
'''

def head(lines: list[str], n: int) -> list[str]:
    return lines[:n]