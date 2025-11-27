'''
Consider a sequence u where u is defined as follows:

    The number u(0) = 1 is the first one in u.
    For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:

dbl_linear(10) should return 22
Note:

Focus attention on efficiency

'''

def dbl_linear(n):
    u = [1]
    ix_y = 0  # pointer for 2*x + 1
    ix_z = 0  # pointer for 3*x + 1

    while len(u) <= n:
        y = 2 * u[ix_y] + 1
        z = 3 * u[ix_z] + 1

        if y < z:
            u.append(y)
            ix_y += 1
        elif y > z:
            u.append(z)
            ix_z += 1
        else:  # y == z, avoid duplicates
            u.append(y)
            ix_y += 1
            ix_z += 1

    return u[n]

print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(1000000))
print(dbl_linear(5))
print(dbl_linear(6))
print(dbl_linear(7))