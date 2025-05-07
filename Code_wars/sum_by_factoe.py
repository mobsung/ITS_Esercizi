'''
Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.
Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

    It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

    In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.


TEST:
    a = [12, 15]
    test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

    a = [15,21,24,30,45]
    test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])

    a = [15,21,24,30,-45]
    test.assert_equals(sum_for_list(a), [[2, 54], [3, 45], [5, 0], [7, 21]])

    a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
    b = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
    test.assert_equals(sum_for_list(a), b)

    a = [-29804, -4209, -28265, -72769, -31744]
    b = [ [2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804] ]
    test.assert_equals(sum_for_list(a), b)
'''


def sum_for_list(lst: list[int]):
    
    prime_dividend:dict[int, list[tuple[int,int]]] = {}

    for num in lst:
        temp_num = num
        for i in range(2, abs(temp_num) + 1):
            
            while temp_num % i == 0:
                if temp_num % i == 0:
                    print(f'DIV -> {i} - Num -> {num} - TEMP num -> {temp_num}')
                    if i not in prime_dividend.keys():
                        prime_dividend[i] = [num]
                    else:
                        prime_dividend[i].append(num) if num == temp_num else None
                    temp_num /= i

    s_prime_dividend = sorted(prime_dividend, key = lambda k: k)
    result = []
    for i in range(len(prime_dividend)):
        result.append([s_prime_dividend[i], sum(prime_dividend[s_prime_dividend[i]])])

    print(prime_dividend)
    return result


a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
b = [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
print(b)
print(sum_for_list(a))
