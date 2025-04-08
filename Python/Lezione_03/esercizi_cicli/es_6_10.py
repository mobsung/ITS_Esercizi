'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.'''




favourite_numbers:list[str, int] = {
                                    "Marcel": (73, 21), 
                                    "Stefano": (6, 9), 
                                    "Lorenzo": (23, 32), 
                                    "Leandro": (11, 99), 
                                    "Valentina": (16, 61)
                                    }

for name, number in favourite_numbers.items():
    print(f"{name}: {number}")