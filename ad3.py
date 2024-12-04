import re

MUL_REGEX = r'mul\((\d+),(\d+)\)'

matches = []

with open("input3") as file:
    for line in file:
        matches += re.findall(MUL_REGEX, line)

ans = 0

for match in matches:
    ans += int(match[0]) * int(match[1])

print(ans)