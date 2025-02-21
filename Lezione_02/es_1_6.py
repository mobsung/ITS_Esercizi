'''1-6. Inserire all'interno di un dizionario il menu' di un ristorante, che viene specificato alla fine della traccia di questo esercizio.
Aggiungere in un nuovo dizionario chiamato ordine, un primo, un secondo, un contorno, una bevanda ed un dolce preso dal menu'. 
Stampare a schermo il conto totale che il cliente dovrà pagare. 
ITS Bakery Menu':
Pizza: 9.00 euro
Pasta: 10.50 euro
Zuppa : 7.00 euro
Hamburger: 15.50 euro
Cotoletta: 10.00 euro
Salmone: 20.20 euro
Patatine Fritte: 5.50 euro
Patate al forno: 5.50 euro
Verdura del giorno: 7.00 euro
Cheesecake: 6.00 euro
Tiramisu': 6.00 euro
Focaccia con Nutella: 6.00 euro
Coca Cola: 3.50 euro
Acqua: 1.50 euro
Vino: 5.00 euro'''



ITS_Bakery_Menu:dict = {
    "Pizza": 9.00, 
    "Pasta": 10.50, 
    "Zuppa" : 7.00, 
    "Hamburger": 15.50, 
    "Cotoletta": 10.00, 
    "Salmone": 20.20, 
    "Patatine fritte": 5.50, 
    "Patate al forno": 5.50, 
    "Verdura giorno": 7.00, 
    "Cheesecake": 6.00,
    "Tiramisu": 6.00, 
    "Focaccia con Nutella": 6.00, 
    "Coca Cola": 3.50,
    "Acqua": 1.50, 
    "Vino": 5.00 
    }
ordine:dict = {} 
ordine["Pizza"] = 9.00
ordine["Salmone"] = 20.20
ordine["Tiramisu"] = 6.00
ordine["Coca Cola"] = 3.50
    
prezzo:int = 0
prezzo += ordine["Pizza"]
prezzo += ordine["Salmone"]
prezzo += ordine["Tiramisu"]
prezzo += ordine["Coca Cola"]
print(f"il tuo ordine è: {' <> '.join(ordine)}")
print(f"Il tuo ordine costa: {prezzo} euro")











