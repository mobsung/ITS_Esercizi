'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program's list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

'''

cube_list:list[int] = []
for number in range(1, 10):
    cube_list.append(number ** 3)
print(f"The first three items in the list are: {cube_list[:3]}")
print(f"Three items from the middle of the list are: {cube_list[3:6]}")
print(f"The last three items in the list are: {cube_list[6:9]}")

