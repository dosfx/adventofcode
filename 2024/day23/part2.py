from itertools import combinations


with open("input.txt") as file:
    connections = dict[str, set[str]]()
    for line in map(str.strip, file):
        a, b = line.split("-")
        connections[a] = connections.get(a, set()) | {b}
        connections[b] = connections.get(b, set()) | {a}

for size in range(len(next(iter(connections.values()))) + 1, 2, -1):
    print(size)
    for node, conns in connections.items():
        for cur in combinations(set([node]) | conns, size):
            for a, b in combinations(cur, 2):
                if not a in connections[b]:
                    break
            else:
                print(",".join(sorted(cur)))
                exit()
