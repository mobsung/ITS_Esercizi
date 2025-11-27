'''
Per documentare una reazione registra serie di simboli compressi: usa `rle(s)` costruendo una lista di `(carattere, conteggio)` per gruppi consecutivi; se `s` è vuota, `[]`. Mantieni la firma e titola i test.
'''

def rle(s: str) -> list[tuple[str,int]]:
    
    if not s:
        return []
    
    result: list[tuple[str,int]] = []
    count: int = 1
    temp_char: str = s[0]

    for char in s[1:]:
        if char == temp_char:
            count += 1
        else:
            result.append((temp_char, count))
            temp_char = char
            count = 1

    result.append((temp_char, count))
    
    return result

print(rle('aaabbc'))


