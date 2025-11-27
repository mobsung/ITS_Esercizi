'''
Se l'indicatore non stampa nulla, versa il tampone di sicurezza. Implementa `read_safe(text, default='')` tornando `text` se esiste, altrimenti `default`. Nessun trimming, nessuna conversione. Mantieni la firma e promuovi i test.
'''


def read_safe(text: str | None, default: str = '') -> str:

    return text if text != None else default


