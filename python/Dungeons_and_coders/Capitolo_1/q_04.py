'''
Per stabilizzare il rituale travasa i reagenti in fiale di volume costante. Usa `chunk(lst, size)` per ottenere sottoliste di lunghezza `size` (l'ultima può variare). Mantieni la firma e supera i test come una titolazione regolare.
'''

def chunk(lst: list[int], size: int) -> list[list[int]]:

    if len(lst) == 0:
        return []

    if len(lst) <= size or size == 0:
        return [lst]

    result: list[list[int]] = []

    for _ in range(len(lst) // size):

        if len(lst) >= size:
            result.append(lst[:size])
            lst = lst[size:]

    if len(lst) > 0:
        result.append(lst)
    return result

print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)), 