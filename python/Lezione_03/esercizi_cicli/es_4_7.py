'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.'''



number_list:list[int] = []
for i in range(3, 30, 3):
    number_list.append(i)
    print(i)