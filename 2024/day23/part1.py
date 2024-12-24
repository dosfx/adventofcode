from itertools import combinations


with open("input.txt") as file:
    nodes = set[str]()
    connections = set[tuple[str, str]]()
    for line in map(str.strip, file):
        a, b = line.split("-")
        nodes.add(a)
        nodes.add(b)
        connections.add((min(a, b), max(a, b)))

threes = list[tuple[str, str, str]]()
for cur in combinations(sorted(nodes), 3):
    a, b, c = cur
    if not a.startswith("t") and not b.startswith("t") and not c.startswith("t"):
        continue
    if not (a, b) in connections:
        continue
    if not (a, c) in connections:
        continue
    if not (b, c) in connections:
        continue
    threes.append(cur)
print(len(threes))
