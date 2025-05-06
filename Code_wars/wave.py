def wave(people:str):
    # Code here
    wave = []
    people.lower()
    for i in range(len(people)):
        wave.append(people[:i] + (people[i:i+1]).title() + people[i+1:]) if people[i] != " " else None
        
    return wave

print(wave('Two words'))