'''6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. '''



from typing import Any
dog_pet:dict[str, str] = {"animal": "dog", "owner's name": "Marcel"}
cat_pet:dict[str, str] = {"animal": "cat", "owner's name": "Stefano"}
lama_pet:dict[str, str] = {"animal": "lama", "owner's name": "Lorenzo"}

pets:list[str] = [dog_pet, cat_pet, lama_pet]

for animal in pets:
    print(animal)