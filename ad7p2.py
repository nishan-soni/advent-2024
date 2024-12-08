
class Solution:

    def get_input(self):
        map = []
        with open("input7.txt") as file:
            for line in file:
                data = line.strip("\n").split(": ")
                map.append([int(data[0]), [int(n) for n in data[1].split(" ")]])
        
        return map


    def solve(self):
        eqs = self.get_input()
        viable = set()
        ans = 0

        def backtrack(index, cur_total, target, eq_ptr):
            if cur_total > target:
                return

            if index >= len(eqs[eq_ptr][1]):
                if cur_total == target:
                    viable.add(eq_ptr)
                return

            concatinated = int(str(cur_total) + str(eqs[eq_ptr][1][index]))
            backtrack(index + 1, concatinated, target, eq_ptr)
            backtrack(index + 1, cur_total + eqs[eq_ptr][1][index], target, eq_ptr)
            backtrack(index + 1, cur_total * eqs[eq_ptr][1][index], target, eq_ptr)
        
        for i in range(len(eqs)):
            print(f'{i} / {len(eqs)}', end='\r', flush=True)
            backtrack(0, 0, eqs[i][0], i)
        
        for i in range(len(eqs)):
            if i in viable:
                ans += eqs[i][0]
        return ans

s = Solution()

print(s.solve())