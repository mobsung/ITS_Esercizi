'''
Nella stanza di titolazione, solo i campioni con etichetta giusta passano. Con `is_valid_record(x)` ritorna **True** solo per i `dict`, altrimenti **False**. Mantieni la firma e promuovi i test.
'''

def is_valid_record(obj) -> bool:
    return True if isinstance(obj, dict) else False