'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all'interno del della lista, altrimenti False.
'''


def binary_search(nums: list[int], num: int) -> bool:

    while len(nums) > 1:

        if num >= nums[len(nums) // 2]:
            nums = nums[len(nums) // 2:]
        else:
            nums = nums[:len(nums) // 2]
    
    return True if nums[0] == num else False


numbers: list[int] = [1, 4, 5, 6, 8, 11, 17, 24, 31, 32, 36, 38, 40, 41, 42]

print(binary_search(numbers, 18))
print(binary_search(numbers, 17))
print(binary_search(numbers, 40))