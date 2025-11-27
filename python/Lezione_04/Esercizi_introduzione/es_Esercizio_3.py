'''Write a function print_numbers(), which takes a list of numbers as argument.
Using a for loop, print each number one by one.'''


def print_numbers(mylist: list) -> None:
    for element in (mylist):
        print(element)

print_numbers([1, 3, 8, 9])