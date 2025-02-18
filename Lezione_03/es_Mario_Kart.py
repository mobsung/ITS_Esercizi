max_pos:int = 20
posizioni:list = ["st", "nd", "rd", "th"]
posizione:int = int(input("Insert position: "))
for pos in range(max_pos):
    if pos < 4 and pos == posizione:
        print(f"You're position is: {posizione}{posizioni[pos - 1]} place.")
        break
    elif pos > 3:
        print(f"You're position is: {posizione}{posizioni[3]} place.")
        break





