'''8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''


def unique_list(sample_list: list) -> list:
    unique_list:list = []
    for number in sample_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

print(unique_list([1,2,3,3,3,3,4,5]))
        