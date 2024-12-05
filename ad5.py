import collections

prev_map = collections.defaultdict(list)

updates = []

def get_input():
    with open("input5.txt") as file:
        line = "_"

        while line != "":
            line = file.readline().strip("\n")
            if line == "":
                continue
            before_after = line.split("|")
            before, after = before_after[0], before_after[1]
            prev_map[after].append(before)
        
        line = "_"
        while line != "":
            line = file.readline().strip("\n")
            if line == "":
                continue
            updates.append(line.split(","))

def evaluate(update):
    visit = set()

    for i in range(len(update) - 1, -1, -1):
        page = update[i]
        visit.add(page)

        for prev_pages in prev_map[page]:
            if prev_pages in visit:
                return 0


    return int(update[len(update) // 2])

get_input()
ans = 0

for u in updates:
    ans += evaluate(u)

print(ans)

