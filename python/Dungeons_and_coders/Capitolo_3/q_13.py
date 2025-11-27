'''
Due distillati rivelano impurità reciproche: registra i componenti esclusivi. Con `symdiff_sorted(a, b)` ritorna gli interi che stanno in una sola lista, in ordine crescente. Mantieni la firma e chiarifica i test.
'''

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    
    result: list[int] = []

    combined: list[int] = a + b

    for num in combined:
        if num not in a or num not in b:
            result.append(num)

    return sorted(result)