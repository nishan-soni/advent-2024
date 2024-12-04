import re

MUL_REGEX = r'mul\((\d+),(\d+)\)|(do)\(\)'

matches = []


with open("input3") as file:
    for line in file:
        split = line.split("don't()")
        for part in split:
            matches.extend((re.findall(MUL_REGEX, part)) + [(None, None, "dont")])
        matches.pop() # get rid of extra don't

ans = 0

do = True

for match in matches:
    if match[2] == "dont":
        do = False
        continue
    elif match[2] == "do":
        do = True
        continue
    
    if do:
        ans += int(match[0]) * int(match[1])

print(ans)