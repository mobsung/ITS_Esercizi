'''8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.'''

from typing import Any

def make_album(name:str, album:str, songs_number:int = None):
    if songs_number is None:
        mydict: dict[str, Any] = {"Artist name": name, "Album name": album}
        return mydict
    else:
        mydict: dict[str, Any] = {"Artist name": name, "Album name": album, "Number of songs": songs_number}
        return mydict


def print_album(mydict):  
    for key, value in mydict.items():
        if key != "Number of songs":
            print(f"{key}: '{value}'", end = " - ")
        else:
            print(f"{key}: {value}", end = " - ")
    print("\n")
        

print_album(make_album("Evanescence", "Fallen", 11))
print_album(make_album("Broken Q", "Prelude to Darkness", 10))
print_album(make_album("AC/DC", "Back in Black"))