'''
Quando la soluzione è pronta, trascrivila in righe separate. `to_json_lines(records)` deve creare una lista di stringhe ottenute serializzando ogni dizionario. Mantieni la firma e promuovi i test.
'''

import json

def to_json_lines(records: list[dict]) -> list[str]:
    if not records:
        return []

    result: list[str] = []

    for record in records:
        result.append(json.dumps(record))


    return result

dati = {"nome": "Luca", "età": 30}
json_str = json.dumps(dati)


print(to_json_lines([{'a':1},{'b':2}]))
print(to_json_lines([]))
print(to_json_lines([{}]))
print(to_json_lines([{'x':1}]))
print(to_json_lines([{'k':9}]))
print(to_json_lines([{'m':0}]))