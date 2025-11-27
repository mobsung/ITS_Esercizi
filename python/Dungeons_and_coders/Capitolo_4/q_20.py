'''
Per risvegliare il golem di Fibonacci registra in un grimorio i risultati parziali: usa `fib_memo(n)` per ottenere l'ennesimo numero evitando di rifare gli stessi passaggi. Mantieni la firma e titola i test.
'''

def fib_memo(n: int) -> int:
    
    a: int = 0
    b: int = 1

    if n == 0:
        return 0

    for _ in range(n - 1):
        b_temp: int = b
        b = b_temp + a
        a = b_temp


    return b

print(fib_memo(0))

'0 1 1 2 3 5 8 13 21'