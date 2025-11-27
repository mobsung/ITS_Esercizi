
result = ""

for i in range(22):
    if i > 0:    
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz, "
        elif i % 3 == 0:
            result += "Fizz, "
        elif i % 5 == 0:
            result += "Buzz, "
        else:
            result += f'{i}, '
print(result)