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
○ Se l’input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com’è.
Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]
'''


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:

    result_intervals: list[list[int]] = []
    v_intervals: list[list[int]] = []
    len_intervals = len(intervals)
    intervals = sorted(intervals)
    cur_interval: list[int] = intervals[0]
    temp_interval: list[int] = intervals[0]

    for interval in intervals:
        for iter in range(len(intervals)):
            if interval not in v_intervals:
                print(f'v_intervals - {v_intervals}')
                if interval[0] <= cur_interval[0] and interval[1] >= cur_interval[0]:
                    temp_interval[0] = interval[0]
                else:
                    temp_interval[0] = cur_interval[0]
                if interval[1] >= cur_interval[0] and interval[1] >= cur_interval[1]:
                    temp_interval[1] = interval[1]
                else:
                    temp_interval[1] = cur_interval[1]
                if cur_interval[1] < interval[0]:
                    cur_interval = interval[:]
                print(f'Interval - {interval}')
                v_intervals.append(interval[:])
        result_intervals.append(temp_interval[:])

    return result_intervals

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))