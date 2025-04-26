'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51
'''

def print_seq(): 
    
    print("Sequenza a):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(1, 8):
        print(i)
    print()
    print("Sequenza b):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(3, 24, 5):
        print(i)
    print()
    print("Sequenza c):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(20, -11, -6):
        print(i)
    print()
    print("Sequenza d):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(19, 52, 8):
        print(i)
    
    return


if __name__ == "__main__":
    print_seq()