
HORIZONTAL_DIRECTS = [(0, 1), (0, -1)]
        
DIAG_DIRECTS = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

VERTICAL_DIRECTS = [(1, 0), (-1, 0)]

WORD = "XMAS"

def in_bounds_and_valid(r, c, ROWS, COLS, word_index, word, grid):

    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or word[word_index] != grid[r][c]:
        return 0
    return 1
        


def find(direct, r, c, ROWS, COLS, word, grid):
    valids = []
    for d in direct:
        dr, dc = d
        nr, nc = r, c
        valid = 1
        for i in range(len(word)):
            valid &= in_bounds_and_valid(nr, nc, ROWS, COLS, i, word, grid)
            nr, nc = dr + nr, dc + nc
        valids.append(valid)

    return valids
            

def search(word):
    grid = []
    ans = 0
    with open("input4") as file:
        for line in file:
            grid.append(list(line.strip("\n")))

    ROWS = len(grid)
    COLS = len(grid[0])


    for r in range(ROWS):
        for c in range(COLS):
            for directions in [HORIZONTAL_DIRECTS, VERTICAL_DIRECTS, DIAG_DIRECTS]:
                ans += sum(find(directions, r, c, ROWS, COLS, word, grid))
    
    return ans

print(search(WORD))
