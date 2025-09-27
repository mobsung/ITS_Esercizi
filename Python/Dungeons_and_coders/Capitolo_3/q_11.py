'''
Nel giardino delle essenze annoti quante specie davvero distinte sono state raccolte. Usa `unique_count(nums)` per restituire il conteggio degli interi unici in `nums`. Mantieni la firma e lascia che i test profumino di rigore.
'''

def unique_count(nums: list[int]) -> int:
    
    amount: int = 0

    for _ in set(nums):
        amount += 1

    return amount


