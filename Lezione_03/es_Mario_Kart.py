posizioni:list = ["st", "nd", "rd", "th"]
max_pos:int = len(posizioni) + 1
posizione:int = int(input("Insert position: "))
for pos in range(max_pos):
    if pos < 4 and pos == posizione:
        print(f"You're position is: {posizione}{posizioni[pos - 1]} place.")
        break
    elif pos > 3:
        print(f"You're position is: {posizione}{posizioni[3]} place.")
        break

