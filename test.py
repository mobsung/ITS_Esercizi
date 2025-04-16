a = {"x0": "y0", "x1": "y1", "x2": "y2"}
c = a

b = {}

for i in range(len(a)):
    for key, value in a.items():
        if i not in b:
            print(f'{i} - {key} - {value}')
            b[i] = (key, value)
       
        
print(b)


# dict1 = {"z0": "v0", "z1": "v1", "z2": "v2"}

# for key, value in dict1.items():

#     print(key, value)