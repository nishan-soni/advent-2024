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
                return update


    return None

get_input()
bad = []

for u in updates:
    ans = evaluate(u)
    if ans:
        bad.append(ans)

def sort(bad_update):
    next_map = collections.defaultdict(list)
    bad_update_set = set(bad_update)

    for page in bad_update:
        for nbr in prev_map[page]:
            if nbr in bad_update_set:
                next_map[nbr].append(page)
    visit = set()
    res = []

    # topo sort
    def dfs(page):
        if page in visit:
            return
        
        visit.add(page)

        for nbr in next_map[page]:
            dfs(nbr)
        
        res.append(page)
    
    for p in bad_update:
        dfs(p)
    res.reverse()
    return int(res[len(res) // 2])


ans = 0
for u in bad:
    ans += sort(u)

print(ans)