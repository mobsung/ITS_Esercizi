'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5'''


def check_each(mylist: list) -> None:
    for element in mylist:
        if  element > 5:
            print(f"{element} is bigger that 5!")
        elif element < 5:
            print(f"{element} is smaller that 5!")
        else:
            print(f"{element} is equal to 5!")

check_each([1, 3, 8, 9, 5])