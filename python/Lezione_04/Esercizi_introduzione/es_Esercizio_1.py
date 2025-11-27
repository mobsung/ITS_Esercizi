'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''

def check_value(n: int) -> None:
    if n > 5:
        print(f"{n} is bigger that 5!")
    elif n < 5:
        print(f"{n} is smaller that 5!")
    else:
        print(f"{n} is equal to 5!")

check_value(int(input("Digita un numero: ")))