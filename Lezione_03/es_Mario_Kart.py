max_pos:int = 20
posizioni:list = ["st", "nd", "rd", "th"]
posizione:int = int(input("Insert position: "))
for pos in range(max_pos):
    if pos < 4 and pos == posizione:
        print(f"Sei arrivato {posizione}{posizioni[pos - 1]}")
        break
    elif pos > 3:
        print(f"Sei arrivato {posizione}{posizioni[3]}")
        break





