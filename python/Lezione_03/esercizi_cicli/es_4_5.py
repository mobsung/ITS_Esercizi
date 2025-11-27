'''4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.'''



one_to_one_million:list[int] = []
for i in range (1, 1000001):
    one_to_one_million.append(i)
print(f"The list starts with {min(one_to_one_million)} and ends with {max(one_to_one_million)}")