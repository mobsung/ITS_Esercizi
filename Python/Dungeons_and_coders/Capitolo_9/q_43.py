'''
Nel cromatogramma compaiono picchi e artefatti: estrai soltanto i valori affidabili. `safe_parse_int_list(s)` deve dividere su virgole, rifilare e aggiungere alla lista **solo** i token convertibili con `int(...)`; gli altri si scartano in silenzio. Mantieni la firma e promuovi i test.
'''

def to_int(x):
    try:
        return int(x)
    except:
        pass

def safe_parse_int_list(s: str) -> list[int]:
    
    return [int(x) for x in s.split(',') if to_int(x) != None]


print(safe_parse_int_list('12, sada, 5d, wda, 012'))