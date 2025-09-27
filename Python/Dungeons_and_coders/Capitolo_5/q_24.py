'''
Per separare i metalli nobili, cataloga i numeri primi fino alla soglia. Implementa `primes_up_to(n)` restituendo tutti i primi **≤ n** ordinati; per `n` < `2`, `[]`. Mantieni la firma e promuovi i test.
'''

def primes_up_to(n: int) -> list[int]:

    primes: list[int] = []

    if n < 2:
        return []
    
    for i in range(2, n + 1):
        is_prime = True

        for div in range(2, int(i ** 0.5) + 1):
            if i % div == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes

print(primes_up_to(10))