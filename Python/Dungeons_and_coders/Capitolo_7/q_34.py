'''
Serve un campione gemello su cui sperimentare. Con `copy_list(src)` restituisci una **nuova lista** identica nei dati e nell’ordine. L’originale resta intatto. Mantieni la firma e promuovi i test.
'''

def copy_list(src: list[str]) -> list[str]:
    return src[:]