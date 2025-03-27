

def recursiveCountdown(n: int) -> None:

    # n is negative
    if n < 0:
        print("Error! Inserted number is negative!")

    # n = 0 must stop the recursive process
    elif n == 0:
        print(0)
    
    # other cases
    else:
        print(n) if n % 19 == 0 else None
        recursiveCountdown(n-1)



def recursiveSum(n:int) -> int:
    # n is negative
    if n < 0:
        print("Error! Inserted number is negative!")
        return None
    # if n = 0 recursive process must be stopped
    elif n == 0:
        return 0
    # if n is positive, compute recursive sum
    else:
        return int(n + recursiveSum(n-1))
    

def recursiveSumInRange(a:int, b:int) -> int:
    # if a > b, swap values of a and b
    if a > b:
        # define a temporary variable called temp, containing value of a
        temp:int = a
        # swap values of a and b
        a = b
        b = temp # now b = a
    # if b = a, the recursive process must be stopped
    if b == a:
        return int(a)
    # otherwise, compute the sum recursively
    else:
        return int(b + recursiveSumInRange(a, b-1))

print("Recursive count:")    
recursiveCountdown(100)
print("Recursive sum:")    
print(recursiveSum(995))
print("Sum in range:")
print(recursiveSumInRange(1, 11))