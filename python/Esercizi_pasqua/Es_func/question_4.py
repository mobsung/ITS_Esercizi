'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
For example:

Test	
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) -> {'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([])) -> {}
'''


def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:

    result: dict[str:list[int]] = {}

    for element in voti:

        if element["nome"] not in result:
            result[element["nome"]] = [element["voto"]]
        else:
            result[element["nome"]] += [element["voto"]]
            
    return result


if __name__ == "__main__":

    print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
    print(aggrega_voti([]))