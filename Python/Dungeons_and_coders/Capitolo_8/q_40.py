'''
Quando la soluzione è pronta, trascrivila in righe separate. `to_json_lines(records)` deve creare una lista di stringhe ottenute serializzando ogni dizionario. Mantieni la firma e promuovi i test.
'''

def to_json_lines(lst: list[dict]) -> list[str]:
    
    if not lst:
        return []

    result: list[str] = []

    for elem in lst:
        temp_str: str = ''

        for key, value in elem.items():
            temp_str += '{' + f'"{key}": "{value}"' + ',' + '}'

        result.append(temp_str)

    return result


print(to_json_lines([{'a':1},{'b':2}]))
print(to_json_lines([]))
print(to_json_lines([{}]))
print(to_json_lines([{'x':1}]))
print(to_json_lines([{'k':9}]))
print(to_json_lines([{'m':0}]))