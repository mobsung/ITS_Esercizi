'''
Due ricettari mostrano reagenti condivisi. Distillali con `intersection_sorted(a, b)`, restituendo una lista ordinata degli interi presenti in entrambi, senza ripetizioni. Mantieni la firma e titola i test alla perfezione.
'''

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    

    result: list[int] = []

    for item in a:

        if item not in result and item in b:
            result.append(item)

    result = sorted(list(set(result)))

    return result

h1 = [1,8,6,2,5,4,8,3,7,-2,-1,0]

print(intersection_sorted(h1, [0]))
