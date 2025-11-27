'''
Costruisci un algoritmo che permette di vincere sempre oppure pareggiare (nel caso peggiore) nel gioco tic-tac-toe

1 2 3
4 5 6
7 8 9

'''


win_pattern: dict[int, int] = {
    1: [[1, 2, 3], [1, 4, 7], [1, 5, 9]],
    2: [[1, 2, 3], [2, 5, 7]],
    3: [[1, 2, 3], [3, 6, 9], [3, 5, 7]],
    4: [[1, 4, 7], [4, 5, 6]],
    5: [[1, 5, 9], [2, 5, 8], [3, 5, 9], [4, 5, 6]],
    6: [[3, 6, 9], [4, 5, 6]],
    7: [[1, 4, 7], [3, 5, 7], [7, 8, 9]],
    8: [[2, 5, 8], [7, 8, 9]],
    9: [[1, 5, 9], [3, 6, 9], [7, 8, 9]]
}


grid: list[int] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
best_choice: list[int] = [5, 1, 3, 7, 9, 2, 4, 6, 8]
visual_grid: list[list] = [
    [1, 2, 3]
    [4, 5, 6]
    [6, 8, 9]
]

round: int = 0

player1: bool = False
player2: bool = False

player1_choice: list[list[int]] = []
player2_choice: list[list[int]] = []

while True:

    

    for num in grid:

        pass