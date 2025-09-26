'''
Nel Laboratorio Reale i reagenti sono dispersi. Misura la quantità totale con `sum_list(nums)`, che somma gli interi in `nums`; se non c'è nulla, restituisci `0`. Mantieni la firma e lascia che gli esperimenti (i test) riescano.
'''

def sum_list(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    return sum(nums)