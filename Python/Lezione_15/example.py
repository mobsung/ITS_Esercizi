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

with open(PATH, 'r') as file:
    print(file.read())