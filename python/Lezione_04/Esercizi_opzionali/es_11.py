'''
11. Word Search Puzzle Solver:

Create a function that solves a word search puzzle.
Provide a 2D grid representing the puzzle and a list of words to find.
Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
Output the locations of the found words within the grid.
'''

# word_list:list[str] = ["ROMA", "SOLE", "AMORE", "ANIMA", "OPERA", "ARIA", "UNITA", "OSSA", "ROSA"]


def getGrid() -> list[list[str]]:

    word_grid:list[list[str]] = [

        ['R', 'O', 'M', 'A', 'U', 'N', 'I', 'T', 'A'], 
        ['O', 'P', 'E', 'R', 'A', 'L', 'A', 'M', 'A'], 
        ['S', 'O', 'L', 'E', 'I', 'O', 'M', 'I', 'C'], 
        ['A', 'M', 'O', 'R', 'E', 'L', 'I', 'N', 'A'], 
        ['A', 'N', 'I', 'M', 'A', 'G', 'A', 'T', 'O'], 
        ['I', 'A', 'R', 'I', 'O', 'O', 'N', 'E', 'R'], 
        ['L', 'E', 'S', 'E', 'L', 'E', 'S', 'O', 'P'], 
        ['I', 'O', 'S', 'S', 'A', 'L', 'A', 'M', 'E'], 
        ['A', 'R', 'I', 'N', 'E', 'S', 'C', 'A', 'S']
         
    ]

    return word_grid


def getWordList() -> list[str]:

    word_list:list[str] = ["ROMA", "SOLE", "AMORE", "ANIMA", "OPERA", "ARIA", "UNITA", "OSSA", "ROSA"]

    return word_list


def drawGrid() -> None:

    word_grid:list[list[str]]  = getGrid()
    for row in word_grid:
        print(f"{' '.join(row)}")


def searchWord():
    pass

    # grid:list[list[str]] = getGrid()
    # word_list:list[str] = getWordList()
    # found_words:list[str] = []
    # temp_word:str = ""
    # initial:str = word_list[0][0]

    # for char in word_list[0]:
    #     for row in grid:
    #         for col in row:
                

            


drawGrid()