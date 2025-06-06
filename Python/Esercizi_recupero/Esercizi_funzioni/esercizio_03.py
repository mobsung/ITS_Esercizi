'''
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''


def chooseProduct(products: dict[str, float]) -> dict[str, float]:

    result_dict: dict[str, float] = {}

    for key, value in products.items():
        if value < 50:
            result_dict[key] = round(value * 1.1, 2)

    return result_dict

print(chooseProduct({'a': 2.34, 'b': 51, 'c': 10}))