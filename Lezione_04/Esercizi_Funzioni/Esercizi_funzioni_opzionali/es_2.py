'''2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''

import random
def guess_the_number(number_range, attempts = 3):
    i = 0
    random_number:int = random.randint(0, number_range)

    while i < attempts:
        guess:int = int(input(f"Pick a number between 0 and {number_range}: "))

        if guess > random_number:
            print("Your guess is too high!")
        elif guess < random_number:
            print("Your guess is too low")
        else:
            print("Congratulations you Won!!!")
            return
        attempts -= 1
    print("You lost!!!")

guess_the_number(10)

        

