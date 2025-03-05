'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''



def check_length(string:str) -> None:
    if len(string) > 10:
        print(f"The length of the {string} is bigger that 10!")
    elif len(string) < 10:
        print(f"The length of the {string} is smaller that 10!")
    else:
        print(f"The length of the {string} is equal to 10!")

check_length(input("Digita un parola: "))