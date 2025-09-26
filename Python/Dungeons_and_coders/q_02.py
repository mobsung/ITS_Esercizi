'''
Tra i flaconi ricomposti cerca la concentrazione dominante. Calcolala con `max_or_none(nums)`: torna il massimo, o `None` se non ci sono dati. Mantieni la firma e superi i test come una titolazione perfetta.
'''

def max_or_none(nums: list[int]) -> int | None:
    
    if len(nums) == 0:
        return None
    
    max_num: int = nums[0]

    for num in nums:
        max_num = num if num > max_num else max_num

    return max_num


print(max_or_none([0]))