'''7. Roman Numeral Conversion:

Create a function that converts a given integer to its Roman numeral representation.
Handle numbers from 1 to 3999.
Use a combination of string manipulation and conditional statements to build the Roman numeral.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

m:int = n // 1000
c:int = n //100 - m * 10
d:int = n //10 - m * 100 - c * 10
u:int = n - m* 1000 - c * 100 - d *10
'''

#funzione per la richeista del numero da convertire
def pickNumber() -> int:

    number: int = int(input("What number would you like to represent?\n"
                            "Valid numbers: from 1 to 3999\n===>"))
    
    while number < 0 or number > 3999:
        number = int(input("The number is unavailable?\n"
                            "Valid numbers: from 1 to 3999!\n===>"))
        
    return number

#funzione per la conversione del numero intero in numero romano
def intToRoman() -> str:
    
    int_roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

    number = pickNumber()
    number_copy:int = number
    roman_number = ""

    for key, value in int_roman.items():
        while number >= key:
            number -= key
            roman_number += value

    print(f'The number: {number_copy} is represented as "{roman_number}" in roman numbers!')

intToRoman()

