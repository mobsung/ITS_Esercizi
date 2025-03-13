a = "11"
b = "1"
result = ""
change = ""
temp = ""
if len(a) < len(b):
    print("a < b")
    temp_a = len(b) - len(a)
    a1 = temp_a * "0" + a
    b1 = b
    print(a1, b1)
elif len(a) > len(b):
    print("a > b")
    temp_b = len(a) - len(b)
    b1 = temp_b * "0" + b
    a1 = a
    print(f'[{a1}] [{b1}]')

for i in range(len(a1) - 1, -1, -1):
    print(f'Iterazione: < {i} >')
    if a1[i] == "1" and b1[i] == "0" or a1[i] == "0" and b1[i] == "1" and change == "":
        print(f'a = {a1[i]} - b = {b1[i]} - change = {change}')
        temp = "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "0" or a1[i] == "0" and b1[i] == "1" and change == "1":
        print(f'a = {a1[i]} - b = {b1[i]} - change = {change}')
        temp = "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "1" and change == "":
        print(f'a = {a1[i]} - b = {b1[i]} - change = {change}')
        temp = "0"
        change = "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "1" and change == "1":
        print(f'a = {a1[i]} - b = {b1[i]} - change = {change}')
        temp = "1"
        change = "1"
        result = temp + result 
    elif a1[0] == "1" and b1[0] == "1":
        print(f'a = {a1[i]} - b = {b1[i]} - change = {change}')
        temp = "10"
        result = temp + result 

print(result)





