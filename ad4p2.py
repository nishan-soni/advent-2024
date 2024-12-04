import collections
DIRECT = [(-1, 1), (1, 1), (-1, -1), (1, -1)] # tr, br, tl, bl


def in_bounds_and_valid(r, c, ROWS, COLS, grid):

    return not (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]))

def search(direct):
    grid = []
    ans = 0
    with open("input4") as file:
        for line in file:
            grid.append(list(line.strip("\n")))

    ROWS = len(grid)
    COLS = len(grid[0])


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "A":
                neighbours = []
                valid_space = True
                for dr, dc in direct:
                    nr, nc = r + dr, c + dc
                    if in_bounds_and_valid(nr, nc, ROWS, COLS, grid):
                        neighbours.append(grid[nr][nc])
                    else:
                        valid_space = False
                        break
                
                if not valid_space:
                    continue

                ctr = collections.Counter(neighbours)
                if neighbours[0] != neighbours[-1] and neighbours[1] != neighbours[2] and ctr["S"] == 2 and ctr["M"] == 2:
                    ans += 1


                
    return ans

print(search(DIRECT))