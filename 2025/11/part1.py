with open("input.txt") as f:
    nodes = {}
    for line in f.readlines():
        split = line.split(":")
        nodes[split[0]] = split[1].split()


def walk(cur: str, path: set[str]) -> int:
    if cur == "out":
        return 1
    count = 0
    for node in nodes[cur]:
        if node in path:
            continue
        path.add(node)
        count += walk(node, path)
        path.remove(node)
    return count


print(walk("you", set(["you"])))
