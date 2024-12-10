import bisect

class Memory:
    def __init__(self, length, start_pos, id = None):
        self.length = length
        self.id = id
        self.start_pos = start_pos

class Solution:

    def __init__(self, disk_map: list = [], files: list[Memory] = [], spaces: list[Memory] = []):
        self.disk_map = disk_map
        self.files = files
        self.spaces = spaces

    def get_input(self):
        disk_space = []
        with open("input9.txt") as file:
            for line in file:
                disk_space += list(line.strip("\n"))
        
        file_id = 0
        current_index = 0
        for i in range(len(disk_space)):
            if i % 2 == 0:
                self.files.append(Memory(length=int(disk_space[i]), id = file_id, start_pos=current_index))
                self.disk_map += ([file_id] * int(disk_space[i]))
                file_id += 1
                current_index += int(disk_space[i])
            else:
                self.disk_map += (["."] * int(disk_space[i]))
                self.spaces.append(Memory(length=int(disk_space[i]), start_pos=current_index))
                current_index += int(disk_space[i])
        self.spaces.sort(key=lambda s: [s.length, s.start_pos])

    def solve(self):

        for i in range(len(self.files) - 1, -1, -1):
            file = self.files[i]
            # space_index = bisect.bisect_left(self.spaces, file.length, key= lambda s: s.length)
            space_index = -1
            for e in range(len(self.spaces)):
                if self.spaces[e].length >= file.length and self.spaces[e].start_pos <= file.start_pos:
                    space_index = e
                    break

            if space_index >= 0:
                space = self.spaces[space_index]
                for j in range(space.start_pos, space.start_pos + file.length):
                    self.disk_map[j] = file.id
                
                for j in range(file.start_pos, file.start_pos + file.length):
                    self.disk_map[j] = "."

                self.spaces.pop(space_index)

                if file.length < space.length:
                    self.spaces.append(Memory(space.length - file.length, space.start_pos + file.length))
                    self.spaces.sort(key=lambda s: [s.length, s.start_pos]) # Maybe use a heap

        ans = 0
        for i in range(len(self.disk_map)):
            if self.disk_map[i] == ".":
                continue
            ans += self.disk_map[i] * i
        
        return ans
s = Solution()

s.get_input()

# print(s.disk_map)

print(s.solve())

# print(s.disk_map)


            
