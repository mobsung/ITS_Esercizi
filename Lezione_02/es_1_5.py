'''1-5. Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula
gradiCelsius=5∗(gradiFahrenheit−32)/9
Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.
La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile con una precisione di un decimo di grado.
Un possibile esempio di output potrebbe essere il seguente:
72 gradi Fahrenheit corrispondono a 22.2 gradi Celsius.'''


gradiFahrenheit:int = 72
gradiCelsius:int = 5 * (gradiFahrenheit - 32) / 9
print (f"La temperatura in gradi Celsius equivale a: {gradiCelsius:.2f}°C")

