'''
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
'''

from room import Room

class Building():

    def __init__(self, name:str, address:str, floors:int):
        
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[str] = [] # Lista che tiene conto delle stanze create
        self.room_ids: list[str] = [] # Lista che tiene conto degli'Id delle stanze per non avere duplicati
        
    # Metodo che restituisce il valore dell'intervallo di piani di inizio e fine
    def get_floors(self) -> tuple[int, int]:

        return self.floors
    
    # Metodo che restituisce la lista con gli oggetti Room
    def get_rooms(self) -> list[int]:

        return self.rooms
    
    # Metodo che consente di aggiungere oggetti di tipo Room negli oggetti di tipo Building
    def add_room(self, room: Room) -> None:

        self.room = room
        if self.floors[0] <= room.get_floor() <= self.floors[1] and room.get_id() not in self.room_ids:
            self.rooms.append(room)
            self.room_ids.append(room.get_id())

    # Metodo che rstituisce il valore dell'area totale
    def area(self):

        area: int = 0

        for room in self.rooms:
            area += room.get_area()
        
        return area
        

if __name__ == "__main__":

    # Creazione room1
    room1 = Room(id="Room1", floor=1, seats=15)
    room2 = Room(id="Room2", floor=5, seats=20)
    room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range
    
    # Creazione di un edificio
    building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

    # Test di inizializzazione Building
    print("\nTest di inizializzazione Building:")
    print(f"Nome: {building.name}, Atteso: Test Building")
    print(f"Indirizzo: {building.address}, Atteso: 123 Test St")
    print(f"Piani: {building.floors}, Atteso: (1, 10)")
    print(f"Stanze iniziali: {building.get_rooms()}, Atteso: []")

    # Test aggiunta stanza valida
    building.add_room(room1)
    print("\nDopo aggiunta Room1:")
    print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

    # Test aggiunta stanza su piano non valido
    building.add_room(room3)
    print("\nDopo tentativo di aggiunta Room3 (piano non valido):")
    print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

    # Test aggiunta stanza duplicata
    building.add_room(room1)
    print("\nDopo tentativo di aggiunta duplicato Room1:")
    print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

    # Test calcolo area
    building.add_room(room2)
    print("\nDopo aggiunta Room2:")
    print(f"Area totale: {building.area()}, Atteso: 70")

    # Test rappresentazione in stringa Building
    print("\nRappresentazione in stringa dell'edificio:")
    print(f"Nome Edificio: {building.name}")
    print(f"Indirizzo Edificio: {building.address}")
    print(f"Piani Edificio: {building.get_floors()}")
    print("Stanze nell'edificio:")
    for room in building.get_rooms():
        print(f"ID Stanza: {room.get_id()}, Piano: {room.get_floor()}, Posti: {room.get_seats()}, Area: {room.get_area()}")
    print(f"Area totale dell'edificio: {building.area()}m2")

    # Verifica valori attesi
    atteso_stanze = ["Room1", "Room2"]
    atteso_area = 70
    print(f"\nVerifica finale: Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: {atteso_stanze}")
    print(f"Verifica finale: Area totale: {building.area()}, Atteso: {atteso_area}")