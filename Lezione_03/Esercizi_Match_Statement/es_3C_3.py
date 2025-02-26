'''
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico
'''


oggetti:list[str] = []
for i in range (3):
    oggetto:str = input("Inserisci il nome di un oggetto: ")
    oggetti.append(oggetto)
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")

oggetti:dict[str, bool] = {}
for i in range (3):
    oggetto:str = input("Inserisci il nome di un oggetto: ")
    oggetti[oggetto] = (True)
match oggetti:
    case {"penna": True, "matita": True, "quaderno": True}:
        print("Materiale scolastico")
    case {"pane": True, "latte": True, "uova": True}:
        print("Prodotti alimentari")
    case {"sedia": True, "tavolo": True, "armadio": True}:
        print("Mobili")
    case {"telefono": True, "computer": True, "tablet": True}:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")
