class Solution:

    def get_input(self):
        grid = []
        trailheads = []
        with open("input10.txt") as file:
            for line in file:
                grid.append([int(n) if n != "." else -1 for n in line.strip("\n")])
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    trailheads.append((r, c))
        return trailheads, grid

    def solve(self, trailheads: list[tuple], grid: list[list[int]]):

        visit = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        DIRECT = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c, prev=-1):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] - 1 != prev:
                return 0
            
            visit.add((r, c))
            if grid[r][c] == 9:
                return 1
        
            res = 0

            for dr, dc in DIRECT:
                nr, nc = r + dr, c + dc
                res += dfs(nr, nc, grid[r][c])

            return res
        
        ans = 0   
        for tr, tc in trailheads:
            visit = set()
            ans += dfs(tr, tc)
        return ans
s = Solution()
sol = s.solve(*s.get_input())
print(sol)
        
