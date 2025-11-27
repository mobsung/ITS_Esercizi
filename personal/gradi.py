def convert_temperature(gradi:float, to_fahrenheit:bool = True) -> float:
    # cancella ... e definisci i parametri della funzione, 
    #successivamente cancella pass e scrivi il tuo codice
    #(0 °C × 9/5) + 32
    #(32 °F - 32) × 5/9
    if to_fahrenheit == False:
        gradi_celsius:float = (gradi - 32) * 5 / 9
        return f'{gradi_celsius:.1f}'
    else:
        gradi_fahrenheit:float = (gradi * 9 / 5) + 32
        return f'{gradi_fahrenheit:.1f}'
    

print(convert_temperature(32, False))