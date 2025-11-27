

def addBinary(a: str, b: str) -> str:
    dict_bin = {"101": "01", "011": "01","100": "10", "010": "10", "111": "11", "110": "01", "000": "00", "001": "10"}
    result = ""
    change = "0"
    temp = ""
    a1, b1 = a, b
    if len(a) < len(b):
        temp_a = len(b) - len(a)
        a1 = temp_a * "0" + a
    elif len(a) > len(b):
        temp_b = len(a) - len(b)
        b1 = temp_b * "0" + b
    if len(a1) == 1 and len(b1) == 1: 
        a1 += "0"
        b1 += "0"

    for i in range(len(a1) - 1, -1, -1):
        temp_val = a1[i] + b1[i] + change
        print(temp_val)
        if i == 0:
            if temp_val == "111":
                temp = "11"
                result = temp + result
            elif temp_val == "000":
                temp = "0"
                result = temp + result
            elif temp_val == "100" or temp_val == "010":
                temp = "1"
                result = temp + result
            else:
                temp = "10"
                result = temp + result
        elif i > 0 and temp_val in dict_bin.keys():
            temp = dict_bin[temp_val][0]
            change = dict_bin[temp_val][1]
            result = temp + result
        print(result)
    if len(a) == 1 and len(b) == 1:
        print(1)
        return result[:-1]
    else:
        print(2)
        return result

print(addBinary(a = "0", b = "0"))