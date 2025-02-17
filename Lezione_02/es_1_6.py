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
print(f"il tuo ordine è: {ordine}")
print(f"Il tuo ordine costa: {prezzo} euro")











