'''
Le pergamene si coprono di incisioni: conta quante volte ogni simbolo riappare, ignorando le macchie. Applica `letter_count(text)` per conteggiare solo lettere (in minuscolo), escludendo tutto il resto. Mantieni la firma e promuovi i test.
'''

def letter_count(text: str) -> dict[str,int]:
    
    count: dict[str,int] = {}

    for char in text:
        if char.isalpha():
            l_cahar = char.lower()
            if l_cahar not in count:
                count[l_cahar] = 1
            else:
                count[l_cahar] += 1

    return count

print(letter_count('AA'))