'''
Per tarare il banco servono misure con parità perfetta: usa `count_even(nums)` per contare quanti valori sono **pari** (compreso `0`). Mantieni la firma e promuovi i test.
'''

def count_even(nums: list[int]) -> int:
    even: int = 0

    for num in nums:
        if num % 2 == 0:
            even += 1

    return even