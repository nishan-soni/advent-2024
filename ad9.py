class Solution:

    def __init__(self, disk_map: list = []):
        self.disk_map = disk_map

    def get_input(self):
        disk_space = []
        with open("input9.txt") as file:
            for line in file:
                disk_space += list(line)
        
        space_id = 0
        for i in range(len(disk_space)):
            if i % 2 == 0:
                self.disk_map += ([space_id] * int(disk_space[i]))
                space_id += 1
            else:
                self.disk_map += (["."] * int(disk_space[i]))

    def move_left_ptr(self, l_ptr):
        while self.disk_map[l_ptr] != "." and l_ptr < len(self.disk_map):
            l_ptr += 1
        return l_ptr

    def move_right_ptr(self, r_ptr):
        while self.disk_map[r_ptr] == "." and r_ptr >= 0:
            r_ptr -= 1
        
        return r_ptr

    def solve(self):        
        l_ptr, r_ptr = 0, len(self.disk_map) - 1

        l_ptr = self.move_left_ptr(l_ptr)
        r_ptr = self.move_right_ptr(r_ptr)

        while l_ptr < r_ptr:
            self.disk_map[l_ptr] = self.disk_map[r_ptr]
            self.disk_map[r_ptr] = "."

            l_ptr = self.move_left_ptr(l_ptr)
            r_ptr = self.move_right_ptr(r_ptr)
        
        ans = 0

        for i in range(len(self.disk_map)):
            if self.disk_map[i] == ".":
                break
            
            ans += self.disk_map[i] * i
        
        return ans
    
s = Solution()

s.get_input()

print(s.solve())

            
