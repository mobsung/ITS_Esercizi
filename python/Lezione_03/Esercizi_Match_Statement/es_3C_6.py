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

mammiferi_terra:list[str] = ["cane", "gatto", "cavallo", "elefante", "leone"]
mammiferi_acqua:list[str] = ["balena", "delfino"]
rettili_terra:list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
rettili_acqua:list[str] = ["tartaruga", "coccodrillo"]
uccelli_terra:list[str] = ["anatra", "gallina", "tacchino"]
uccelli_aria:list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra"]
pesci:list[str] = ["squalo", "trota", "salmone", "carpa"]

animal:str = input("Digita il nome di un animale: ").lower()
habitat:str = input(f"Digita l'habitat in cui vive l'animale {animal}:").lower()

#animal_info:dict[str, str] = {}

match animal:
    case animal if animal in (mammiferi_terra) and habitat == "terra":
        animal_type:str = "Mammifero"
        #animal_info[animal] = animal_type, habitat
    case animal if animal in (mammiferi_acqua) and habitat == "acqua":
        animal_type:str = "Mammifero"
        #animal_info[animal] = animal_type, habitat
    
    case animal if animal in (rettili_terra) and habitat == "terra":
        animal_type:str = "Rettile"
        #animal_info[animal] = animal_type, habitat
    case animal if animal in (rettili_acqua) and habitat == "acqua":
        animal_type:str = "Rettile"
        #animal_info[animal] = animal_type, habitat

    case animal if animal in (uccelli_terra) and habitat == "terra":
        animal_type:str = "Uccello"
        #animal_info[animal] = animal_type, habitat
    case animal if animal in (uccelli_aria) and habitat == "aria":
        animal_type:str = "Uccello"
        #animal_info[animal] = animal_type, habitat

    case animal if animal in (pesci) and habitat == "acqua":
        animal_type:str = "Pesce"
        #animal_info[animal] = animal_type, habitat

    case _:
        animal_type:str = "unknown"
        print(animal_type)
print(f"L'animale {animal} è un {animal_type} e vive nel habitat {habitat}")