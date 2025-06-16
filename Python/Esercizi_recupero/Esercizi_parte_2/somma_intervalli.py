'''
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.
Requisiti:
● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].
● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
○ Se l'input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com'è.
Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]
'''


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:

    intervals = sorted(intervals)
    result_intervals: list[list[int]] = []

    while len(intervals) > 0:

        cur_interval: list[int] = intervals[0].copy()

        for interval in intervals.copy():
            if cur_interval[0] <= interval[0] and cur_interval[1] > interval[1]:
                cur_interval: list[int] = [cur_interval[0], cur_interval[1]]
                intervals.remove(interval)

            elif cur_interval[0] <= interval[0] <= cur_interval[1]:
                cur_interval: list[int] = [cur_interval[0], interval[1]]
                intervals.remove(interval)

        result_intervals.append(cur_interval)
    return result_intervals


print(merge_intervals([[1, 4], [4, 5]])) # restituisce [[1, 5]]
print(merge_intervals([[1, 4], [2, 6], [8, 10], [15, 18]])) # restituisce [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 3], [2, 2], [4, 8], [8, 10], [1, 18]])) # restituisce [[1, 18]]