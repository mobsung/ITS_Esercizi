def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    result_dict:dict[str, int] = {}
        
    for key in dict1:
        if key not in result_dict:
            if key in dict2:
                result_dict[key] = dict1[key] + dict2[key]
            else:
                result_dict[key] = dict1[key]

    for key in dict2:
        if key not in result_dict:
            result_dict[key] = dict2[key]

    return result_dict

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#{'a': 1, 'b': 5, 'c': 4}