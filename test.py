from typing import TYPE_CHECKING

# a = {"x0": "y0", "x1": "y1", "x2": "y2"}
# b = {}

# for i, (key, value) in enumerate(a.items()):
#     b[i] = (key, value)

# print(b)

# a = 'Two words'

# #print(a[:0] + (a[0:]).title())
# print(a.title())


u = ['a', 'b', 'c']

u.insert(u.index("b"), 'd')
u.pop(u.index("b"))
print(u)