'''

Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

For example:
Test 	Result

print(frequency_dict(['mela', 'banana', 'mela']))

	

{'mela': 2, 'banana': 1}
'''

def frequency_dict(elements: list) -> dict:
    # cancella pass e scrivi il tuo codice
    
    result_dict: dict = {}

    for elem in elements:
        if elem not in result_dict:
            result_dict[elem] = 1
        else:
            result_dict[elem] += 1

    return result_dict

print(frequency_dict(['mela', 'banana', 'mela']))
