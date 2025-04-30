a = {"x0": "y0", "x1": "y1", "x2": "y2"}
b = {}

for i, (key, value) in enumerate(a.items()):
    b[i] = (key, value)

print(b)