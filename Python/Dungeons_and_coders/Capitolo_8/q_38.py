'''
Nel reticolo delle misure i numeri compaiono ovunque: `json_sum_numbers(data)` li sommi tutti attraversando dizionari e liste in profondità. Mantieni la firma e promuovi i test.
'''

def json_sum_numbers(obj) -> float:
    
    result: int | float = 0
    if isinstance(obj, int) or isinstance(obj, float):
        return obj 

    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, int) or isinstance(value, float):
                result += value
            
            if isinstance(key, int) or isinstance(key, float):
                result += key
            
            if isinstance(value, list) or isinstance(value, dict):
                result += json_sum_numbers(value)

    if isinstance(obj, list):
        for depth in obj:
            if isinstance(depth, int) or isinstance(depth, float):
                result += depth

            if isinstance(depth, list) or isinstance(depth, dict):
                result += json_sum_numbers(depth)

    return result

print(json_sum_numbers({'a':{'b':2.5}}))
print(json_sum_numbers({'x':[1,2,3]}))
print(json_sum_numbers(7))
