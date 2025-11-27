'''
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))


{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
{'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}

'''

from typing import Any

def create_contact(name: str, email: str = None, telefono: int = None) -> dict:

    contact:dict[str, Any] = {}

    contact["profile"] = name
    contact["email"] = email if email != None else None
    contact["telefono"] = telefono if telefono != None else None

    return contact

def update_contact(dictionary: dict, name: str, email: str = None, telefono: int = None) -> dict:

    dictionary.update({"profile": name}) if name != None else None
    dictionary.update({"email": email}) if email != None else None
    dictionary.update({"telefono": telefono}) if telefono != None else None

    return dictionary


if __name__ == "__main__":
    contact = create_contact("Mario Rossi", email = "mario.rossi@gmail.com", telefono = 788787)
    print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono = 788787))
    print(update_contact(contact, "Mario Rossi", telefono = 123456789))