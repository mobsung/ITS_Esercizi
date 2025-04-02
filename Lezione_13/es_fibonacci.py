


def fibonacci(n:int) -> int:
    # n is negative or 0
    if n <= 0:
        return 0
    # n = 1
    elif n == 1:
        return 1
    # otherwise, compute Fibonacci series applying its formula
    else:
        return int(fibonacci(n-1) + fibonacci(n-2))
    

if __name__ == "__main__":

    print(fibonacci(35))