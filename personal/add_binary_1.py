
def addBinary(a: str, b: str) -> str:
    result = ""
    change = ""
    temp = ""
    if len(a) < len(b):
        temp_a = len(b) - len(a)
        a1 = temp_a * "0" + a
        b1 = b
    elif len(a) > len(b):
        temp_b = len(a) - len(b)
        b1 = temp_b * "0" + b
        a1 = a


    for i in range(len(a1) - 1, -1, -1):
        if a1[i] == "1" and b1[i] == "0" and change == "" or a1[i] == "0" and b1[i] == "1" and change == "":
            temp = "1"
            change = ""
            result = temp + result
        elif a1[i] == "1" and b1[i] == "0" and change == "1" or a1[i] == "0" and b1[i] == "1" and change == "1":
            temp = "0"
            change = "1"
            result = temp + result
        elif a1[i] == "1" and b1[i] == "1" and change == "":
            temp = "0"
            change = "1"
            result = temp + result
        elif a1[i] == "1" and b1[i] == "1" and change == "1":
            temp = "1"
            change = "1"
            result = temp + result
        elif a1[i] == "0" and b1[i] == "0" and change == "1":
            temp = "1"
            change = ""
            result = temp + result
        elif a1[i] == "0" and b1[i] == "0" and change == "":
            temp = "0"
            change = ""
            result = temp + result
        elif a1[0] == "1" and b1[0] == "1":
            temp = "10"
            result = temp + result
    result = change + result
    return result

print(addBinary(a = "110110", b = "1100"))