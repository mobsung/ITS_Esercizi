'''
Nella sala delle spirali raccogli le gocce fino all'ultima: implementa `range_sum(n)` per sommare da `1` a `n`; se il contenitore (`n`) non ha volume (≤ `0`), restituisci `0`. Mantieni la firma e lascia che gli esperimenti (i test) riescano.
'''

def range_sum(n: int) -> int:
    if n <= 1:
        return n
    
    result: int = 0

    for i in range(n + 1):
        result += i
    
    return result

print(range_sum(3))