'''
Gli alambicchi accumulano residui: separa ogni sostanza tenendo solo la prima apparizione. Usa `dedup_stable(nums)` per ottenere una nuova lista senza duplicati successivi, in ordine. Mantieni la firma e supera i test come un filtraggio riuscito.
'''

def dedup_stable(nums: list[int]) -> list[int]:

    if len(nums) == 0:
        return nums

    new_nums: list[int] = [nums[0]]

    for num in nums:
        if num  != new_nums[-1]:
            new_nums.append(num)

    return new_nums

print(dedup_stable([-4, -2, 2, 7, 0, 0, 7, 8, 9, 7]))