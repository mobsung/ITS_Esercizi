'''
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula
'''

class Room():

    id_list:list[str] = [] # lista che tiene conto degli'ID già inseriti in qunto non devono ripetersi 

    def __init__(self, id:str, floor:int, seats:int):
        
        self.set_id(id)
        self.set_floor(floor)
        self.set_seats(seats)
        Room.id_list.append(id)

    # funzione che retitituisce il valore dell'ID
    def get_id(self) -> str:
        
        return self.id

    # funzione che restituisce il valore del piano 
    def get_floor(self) -> int:
        
        return self.floor

    # funzione che restituisce il valore dei posti 
    def get_seats(self) -> int:
        
        return self.seats

    # funzione che restituisce il valore dell'area data dal numero di posti * 2
    def get_area(self) -> int:
        
        return self.seats * 2
    
    
    # funzione per inpostare l'id e che controlla che non sia già in uso
    def set_id(self, id:str) -> None:

        self.id = id


    # funzione per impostare il piano
    def set_floor(self, floor:int) -> None:

        if type(floor) != int:
            print("The floor should be an integer")
        else:
            self.floor = floor


    # funzione per impostare il numero di posti
    def set_seats(self, seats:int) -> None:

        if type(seats) != int:
            print("The seats should be a positive integer")
        else:
            self.seats = seats


if __name__ == "__main__":
    
    room1 = Room(id="Room1", floor=1, seats=15)
    room2 = Room(id="Room2", floor=5, seats=20)
    room3 = Room(id="Room3", floor=11, seats=10)

    print("Test classe Room1:")
    print(f"ID: {room1.get_id()}, Atteso: Room1")
    print(f"Piano: {room1.get_floor()}, Atteso: 1")
    print(f"Posti: {room1.get_seats()}, Atteso: 15")
    print(f"Area: {room1.get_area()}, Atteso: 30")

    print("Test classe Room2:")
    print(f"ID: {room2.get_id()}, Atteso: Room2")
    print(f"Piano: {room2.get_floor()}, Atteso: 5")
    print(f"Posti: {room2.get_seats()}, Atteso: 20")
    print(f"Area: {room2.get_area()}, Atteso: 40")

    print("Test classe Room3:")
    print(f"ID: {room3.get_id()}, Atteso: Room3")
    print(f"Piano: {room3.get_floor()}, Atteso: 11")
    print(f"Posti: {room3.get_seats()}, Atteso: 10")
    print(f"Area: {room3.get_area()}, Atteso: 20")