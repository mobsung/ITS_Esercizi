def zero(operand = None): return 0
def one(operand = None): return 1 
def two(operand = None): return 2 
def three(operand = None): return 3 
def four(operand = None): return 4 
def five(operand = None): return 5 
def six(operand = None): return 6 
def seven(operand = None): return 7 
def eight(operand = None): return 8 
def nine(operand = None): return 9 
def plus(a, b = 0): return a + b 
def minus(a, b = 0): return a - b 
def times(a, b = 1): return a * b 
def divided_by(a, b = 1): return a // b 


print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3
