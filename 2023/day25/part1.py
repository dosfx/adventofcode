from typing import Dict, Set

with open("input.txt") as file:
    comps: Dict[str, Set[str]] = {}
    for line in file.readlines():
        id = line[0:3]
        if id not in comps:
            comps[id] = set()
        for other in line[4:].strip().split(" "):
            comps[id].add(other)
            if other not in comps:
                comps[other] = set()
            comps[other].add(id)

s = set(comps)
def count(c: str) -> int:
    return len(comps[c] - s)

while sum(map(count, s)) != 3:
    s.remove(max(s, key=count))

print(len(s) * len(set(comps) - s))
