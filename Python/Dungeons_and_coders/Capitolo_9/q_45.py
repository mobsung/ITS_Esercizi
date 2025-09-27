'''
Nella titolazione finale, una sola impurezza invalida l'intero lotto. `parse_int_list_strict(s)` deve convertire **tutti** i token in interi dopo `strip()`; appena uno fallisce, **lancia `ValueError`**. Caso base: stringa vuota → `[]`. Mantieni la firma e promuovi i test.
'''


def parse_int_list_strict(s: str) -> list[int]:

    if not s.strip():
        return []

    result: list[int] = []
    elements = s.split(",")

    for elem in elements:
        elem = elem.strip()

        try:
            number = int(elem)
        except ValueError:
            raise ValueError
        
        result.append(number)

    return result

