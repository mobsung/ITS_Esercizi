'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''



from typing import Any

def make_album(name:str, album:str, songs_number:int = None) -> dict:
    if songs_number == str(None):
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
        

cont: int = 0
insert= []
while cont <2:
    artista:str = input("Inserisci un artista: ")
    album:str = input("Inserisci un album: ")
    num_songs:int = int(input("Inserisci il numero di canzoni(inserisci 'None' se non disponibile): "))
    insert.append((artista,album,num_songs))
    cont += 1

for i in insert:
    print_album(make_album(i[0],i[1],i[2]))


