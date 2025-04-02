'''9-13. Dice: Make a class Dice with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''

import random

class Dice:

    def __init__(self, sides: int = 6):
        
        self.sides = sides
    

    def roll_die(self) -> None:

        print(f'{random.randint(1, self.sides)}', end = " ")

    
    def setSides(self, sides: int) -> None:

        self.sides = sides


if __name__ == "__main__":

    dice: Dice = Dice()

    print("10 Rolls of the Dice with 6 Sides!")
    for i in range(10):
        dice.roll_die()

    print("\n10 Rolls of the Dice with 10 Sides!")
    dice.setSides(10)
    for i in range(10):
        dice.roll_die()

    print("\n10 Rolls of the Dice with 20 Sides!")
    dice.setSides(20)
    for i in range(10):
        dice.roll_die()