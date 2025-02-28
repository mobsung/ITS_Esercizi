'''Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra
'''

mammiferi:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]

habitat_list:list[str] = ["acqua", "aria", "terra"]

animal:str = input("Digita il nome di un animale: ")
habitat:str = input(f"Digita l'habitat in cui vive l'animale {animal}:")

match animal, habitat:
    case animal if animal in (mammiferi):
        animal_type = "Mammiferi"
        print(f"{animal} appartiene alla categoria dei {animal_type}!")
    case animale if animal in (rettili):
        animal_type = "Rettili"
        print(f"{animal} appartiene alla categoria dei {animal_type}!")
    case animale if animal in (uccelli):
        animal_type = "Uccelli"
        print(f"{animal} appartiene alla categoria dei {animal_type}!")
    case animale if animal in (pesci):
        animal_type = "Pesci"
        print(f"{animal} appartiene alla categoria dei {animal_type}!")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animal}")


