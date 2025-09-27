'''
A fine procedura versa tutto nello stesso crogiolo creando un flusso uniforme. Ottienilo con `flatten_once(nested)`, che concatena le sottoliste a un solo livello. Mantieni la firma e fai riuscire i test.
'''

def flatten_once(nested: list[list[int]]) -> list[int]:
    
    result: list[int] = []

    for lst in nested:
        result += lst
    
    return result
