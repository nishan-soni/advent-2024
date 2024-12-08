import collections


def get_input():
    grid = []
    with open("input6.txt") as file:
        for line in file:
            grid.append(list(line.strip("\n")))

    return grid


def get_gaurd_pos(ROWS, COLS, grid):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "^":
                return (r, c)



DIRECT = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move_gaurd(r, c, direct_ptr, ROWS, COLS):
    cache = set()
    visit = set()
    cycles = 0
    while not (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c, direct_ptr) in cache):
        # if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c, direct_ptr) in cache:
        #     break

        dr, dc = DIRECT[direct_ptr]
        nr, nc = r + dr, c + dc

        if (r, c) in visit:
            cycles += 1
            grid[nr][nc] = "O"

        visit.add((r, c))
        cache.add((r, c, direct_ptr))


        # grid[r][c] = "X"

        if not (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS) and grid[nr][nc] == "#":
            direct_ptr = (direct_ptr + 1) % 4
            dr, dc = DIRECT[direct_ptr]
            nr, nc = r + dr, c + dc

        r, c = nr, nc
    return visit, cycles



grid = get_input()
ROWS = len(grid)
COLS = len(grid[0])

s_r, s_c = get_gaurd_pos(ROWS, COLS, grid)


visit, cycles = move_gaurd(s_r, s_c, 0, ROWS, COLS)
for g in grid:
    print("".join(g))


print(cycles)
