'''
Due etichette di fiale, mischiate, potrebbero descrivere lo stesso composto. Confermalo con `are_anagrams(a, b)` ignorando spazi e maiuscole. Torna `True` se coincidono nelle lettere, altrimenti `False`. Mantieni la firma e chiarisci i test.
'''

def are_anagrams(a: str, b: str) -> bool:

    a1:list[str] = [char for char in a.lower() if char.isalpha()]
    b1:list[str] = [char for char in b.lower() if char.isalpha()]

    a1.sort()
    b1.sort()

    return True if a1 == b1 else False
    
print(are_anagrams('listen','silent'))
print(are_anagrams('ab','aa'))
print(are_anagrams('evil','vile'))
print(are_anagrams('Dormitory','Dirty room'))
print(are_anagrams('a','b'))
print(are_anagrams('Stone','Tones'))