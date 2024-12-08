import collections

class Solution:

    def get_input(self):
        
        positions = collections.defaultdict(list)
        grid = []

        with open("input8.txt") as file:
            for line in file:
                grid.append(list(line.strip("\n")))
        
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] not in (".", "#"):
                    positions[grid[r][c]].append((r, c))

        return positions, grid
    
    def solve(self, positions, grid):

        ROWS = len(grid)
        COLS = len(grid[0])

        unique_antinodes = set()

        for antenna_key in positions:
            for i in range(len(positions[antenna_key])):
                # Caluclate distance between given node and all others
                for j in range(len(positions[antenna_key])):
                    if j == i:
                        continue
                    # Find position of anti node and add it to answer if in bounds
                    delta_r, delta_c = positions[antenna_key][j][0] - positions[antenna_key][i][0], positions[antenna_key][j][1] - positions[antenna_key][i][1]

                    anitnode_r, antinode_c = positions[antenna_key][j][0], positions[antenna_key][j][1]

                    while not(anitnode_r < 0 or antinode_c < 0 or anitnode_r >= ROWS or antinode_c >= COLS):
                        unique_antinodes.add((anitnode_r, antinode_c))
                        anitnode_r, antinode_c = anitnode_r + delta_r, antinode_c + delta_c
        
        return len(unique_antinodes)
        
s = Solution()

print(s.solve(*s.get_input()))