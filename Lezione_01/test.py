a = "11"
b = "1"
result = ""
change = ""
temp = ""
if len(a) < len(b):
    print(f'------1------')
    temp_a = len(b) - len(a)
    a1 = temp_a * "0" + a
    b1 = b
elif len(a) > len(b):
    print(f'------2------')
    temp_b = len(a) - len(b)
    b1 = temp_b * "0" + b
    a1 = a 

for i in range(len(a1) - 1, -1, -1):
    print(f'------3------')
    if a1[i] == "1" and b1[i] == "0" or a1[i] == "0" and b1[i] == "1" and change == "":
        print(f'------4------')
        temp = "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "0" or a1[i] == "0" and b1[i] == "1" and change == "1":
        print(f'------5------')
        temp = "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "1" and change == "":
        print(f'------6------')
        temp == "0"
        change == "1"
        result = temp + result 
    elif a1[i] == "1" and b1[i] == "1" and change == "1":
        print(f'------7------')
        temp == "1"
        change == "1"
        result = temp + result 
    elif a1[0] == "1" and b1[0] == "1":
        print(f'------8------')
        temp = "10"
        result = temp + result 

print(result)





