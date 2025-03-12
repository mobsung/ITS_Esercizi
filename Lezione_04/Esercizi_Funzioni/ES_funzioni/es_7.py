'''7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''


def count_upper_lower(string: str) -> tuple:
    upper:int = 0
    lower:int = 0
    for char in string:
        if char != " ":
            if char == char.lower():
                lower += 1
            else:
                upper += 1
    return lower, upper

lower , upper = count_upper_lower("The quick Brow Fox")

print(f'Lower = {lower}')
print(f'Upper = {upper}')