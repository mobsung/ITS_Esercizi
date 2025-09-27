'''
Il reattore risponde a frequenze 3 e 5: usa `sum_multiples(limit)` per sommare tutte le letture **< limit** divisibili per `3` o `5`. Per `limit` ≤ `0`, restituisci `0`. Mantieni la firma e titola i test.
'''

def sum_multiples(limit: int) -> int:

    if limit <= 0:
        return 0
    
    result: int = 0

    for num in range(limit):

        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result

print(sum_multiples(1))