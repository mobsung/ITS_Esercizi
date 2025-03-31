'''6. Password Generator:

Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
Allow the user to specify the password length and desired character types.
Generate and return a random password that meets the user's criteria.
'''

import random
# funzione per l'input dei parametri della password
def password_parameters() -> tuple[int, int, int, int]:

    chosen_length = int(input("How long should the password be?\n==>"))
    length: int = 0

    while chosen_length != length:
        lower_case: int = int(input("How many lower case characters should it have?\n==>"))
        upper_case: int = int(input("How many uper case characters should it have?\n==>"))
        numbers: int = int(input("How many numbers should it have?\n==>"))
        symbols: int = int(input("How many symbols should it have?\n==>"))
        
        length = lower_case + upper_case + numbers + symbols
        
        if chosen_length == length:
            print(f'The requirements have been met!')
        else:
            print('The comulative length with the number of character isn\'t enough to reach the wanted length!\n'
                  'Choose different values!')

    return lower_case, upper_case, numbers, symbols

#funzione per la generazione delle lettere minuscole
def iterate_lower_case(parameter: int) -> str:

    lower_str: str = "abcdefghijklmnopqrstuvwxyz"
    temp_lower: str = ""
    parameter 

    for i in range(parameter):
        random_index: int = random.randint(0, len(lower_str) - 1)
        temp_lower += lower_str[random_index]

    return temp_lower

#funzione per la generazione delle lettere maiuscole
def iterate_upper_case(parameter: int) -> str:

    upper_str: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp_upper: str = ""

    for i in range(parameter):
        random_index: int = random.randint(0, len(upper_str) - 1)
        temp_upper += upper_str[random_index]

    return temp_upper

#funzione per la generazione dei numeri
def iterate_numbers(parameter: int) -> str:

    numbers_str: str = "0123456789"
    temp_numbers: str = ""

    for i in range(parameter):
        random_index: int = random.randint(0, len(numbers_str) - 1)
        temp_numbers += numbers_str[random_index]

    return temp_numbers

#funzione per la generazione dei symboli speciali
def iterate_symbols(parameter: int) -> str:

    symbols_str: str = "!@#$%^&*-+=|:;<>,.?/~`"
    temp_symbols: str = ""
    
    for i in range(parameter):
        random_index: int = random.randint(0, len(symbols_str) - 1)
        temp_symbols += symbols_str[random_index]

    return temp_symbols

#funzione per la generazione della password
def generate_password() -> str:

    parameter_lower, parameter_upper, parameter_number, parameter_symbol = (password_parameters())

    lower_str = iterate_lower_case(parameter_lower)
    upper_str = iterate_upper_case(parameter_upper)
    numbers_str = iterate_numbers(parameter_number)
    symbols_str = iterate_symbols(parameter_symbol)

    password: list[str] = list(lower_str + upper_str + numbers_str + symbols_str)
    random.shuffle(password)
    

    print(f'Your password is - {''.join(password)}')

generate_password()


