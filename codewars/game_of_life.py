'''
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:
'''

'''[
            [1,1,1,0,0,0,1,0],
            [1,0,0,0,0,0,0,1],
            [0,1,0,0,0,1,1,1]
        ], 16, [
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
        ]

        [
            [1,0,0],
            [0,1,1],
            [1,1,0]
        ]
        [
            [0,1,0],
            [0,0,1],
            [1,1,1]
        ]
'''

def check_neighbours(cells: list[list[int]], row: int, col: int) -> int:

    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    neighbours = 0
    for dr, dc in offsets:
        r, c = row + dr, col + dc
        if 0 <= r < len(cells):
            if 0 <= c < len(cells[r]):
                if cells[r][c] == 1:
                    neighbours += 1
    
    return neighbours


def expanded_cells(cells: list[list[int]]) -> list[list[int]]:

    inverted: list[list[int]] = [[row[i] for row in cells] for i in range(len(cells[0]))]

    if inverted[0].count(1) > 0:
        inverted.insert(0, [0 for _ in range(len(inverted[0]))])
    if inverted[-1].count(1) > 0:
        inverted.append([0 for _ in range(len(inverted[0]))])

    cells: list[list[int]] = [[row[i] for row in inverted] for i in range(len(inverted[0]))]


    if cells[0].count(1) > 0:
        cells.insert(0, [0 for _ in range(len(cells[0]))])
    if cells[-1].count(1) > 0:
        cells.append([0 for _ in range(len(cells[0]))])

    return cells


def strip_empty(cells: list[list[int]]) -> list[list[int]]:


    inverted = list(zip(*cells))

    inverted = [col for col in inverted if any(cell == 1 for cell in col)]

    cells = [list(row) for row in zip(*inverted)]
    
    cells = [row for row in cells if any(cell == 1 for cell in row)]
    
    if not cells:
        return []
    
    return cells


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    
    print('Starting grid:\n')
    print_cells(cells)
    print('\n')
    y: int = 0

    while y < generations:
        cells = expanded_cells(cells)

        current_evolution: list[tuple[int, int, int]] = []

        for row in range(len(cells)):
            for col in range(len(cells[row])):
                if cells[row][col] == 0 and check_neighbours(cells, row, col) == 3:
                    current_evolution.append((row, col, 1))
                elif cells[row][col] == 1:
                    if check_neighbours(cells, row, col) > 3 or check_neighbours(cells, row, col) < 2:
                        current_evolution.append((row, col, 0))

        for row, col, cel in current_evolution:
            cells[row][col] = cel

        print(f'Generation: {y+1}\n')
        print_cells(cells)
        print('\n')
        y += 1
    
    # return cells

def print_cells(cells: list[list[int]]) -> None:
    for row in cells:
        print("".join("⬜" if cell == 1 else "⬛" for cell in row))

# print(check_neighbours([
#             [1,0,0],
#             [0,1,1],
#             [1,1,0]
#         ], 0, 1))

# print_matrix(get_generation([
#             [1,0,0],
#             [0,1,1],
#             [1,1,0]
#         ],6))


# print_cells(get_generation([
#             [1,1,1,0,0,0,1,0],
#             [1,0,0,0,0,0,0,1],
#             [0,1,0,0,0,1,1,1]
#         ], 16))

# get_generation([
#             [0,1,1,0,1,0,1,0,1,1],
#             [1,1,0,1,0,1,0,1,0,0],
#             [0,1,0,1,1,0,1,1,1,0],
#             [0,1,0,1,0,0,1,0,1,1],
#             [1,0,0,1,0,1,1,1,1,0]
#         ], 50)


get_generation([
    [1,0,0,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0]
], 20)