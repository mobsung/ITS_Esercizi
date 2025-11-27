def count_isolated(numbers:list[int]) -> int:
    # cancella ... e definisci parametri e tipo di dato, 
    #successivamente cancella pass e scrivi il tuo codice
    counter:int = 0
    copy_list:list[int] = numbers[:]
    test_list: list[int] = []

    for i in range(1, len(numbers)):
        if i == 1 and numbers[0] != numbers[1]:
            counter +=1
        if i == len(numbers) - 1:
            if numbers[-1] != numbers[-2]:
                counter += 1
        if i < len(numbers) - 1:
            if numbers[i] != numbers[i - 1] and numbers[i] != numbers[i + 1]:
                test_list.append(numbers[i])
                counter += 1
    print(test_list)
                
    return counter


print(count_isolated([1, 2, 3, 4, 5]))
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))