PATH: str = 'Python/Lezione_15/example.txt'

# file = open(PATH, 'r')
# #file.write('WAZAAA!!')
# print(file.read())
# file.close()

# file = open(PATH, 'r')
# try:
#     pass
# finally:
#     file.close()

with open(PATH, 'w') as file:
    print(file.read())

# import json
# with open('Python/Lezione_15/example_json.json', 'w') as file:

#     db: dict = {
#         'aaa': {'a': 'skahkjhf', 'b': 'kuagsdk'},
#         'bbb': {'c': 'skahkjhf', 'd': 'kuagsdk'},
#         'ccc': {'e': 'skahkjhf', 'f': 'kuagsdk'}
#     }

#     json.dump(db, file, indent=4)
