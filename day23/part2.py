from typing import Dict, List, Set, Tuple

Point = Tuple[int, int]

with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

class Node:
    def __init__(self, x: int, y: int, id: int) -> None:
        self.connections: List[Node] = []
        self.points: Set[Point] = set([(x, y)])
        self.id = id

    @property
    def cost(self) -> int:
        return len(self.points)

    def __repr__(self) -> str:
        return chr(ord("a") + (self.id % 26))

width = len(grid[0])
height = len(grid)
node_grid: Dict[Point, Node] = {}
start = Node(1, 0, 0)
end = Node(width - 2, height - 1, 1)
node_grid[(1, 0)] = start
node_grid[(width - 2, height - 1)] = end
id = 2

for y in range(1, height - 1):
    for x in range(1, width - 1):
        if grid[y][x] == "#":
            continue
        node = Node(x, y, id)
        id += 1
        node_grid[(x, y)] = node
        for p in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
            if p in node_grid:
                other = node_grid[p]
                other.connections.append(node)
                node.connections.append(other)

nodes = list(node_grid.values())
while True:
    for i in range(len(nodes)):
        cur = nodes[i]
        if len(cur.connections) > 2:
            continue
        change = False
        for other in cur.connections:
            if len(other.connections) <= 2:
                change = True
                nodes.remove(other)
                cur.connections.remove(other)
                for p in other.points:
                    node_grid[p] = cur
                    cur.points.add(p)
                for other_other in other.connections:
                    if other_other != cur:
                        other_other.connections.remove(other)
                        other_other.connections.append(cur)
                        cur.connections.append(other_other)
        if change:
            break
    else:
        break

# for y in range(height):
#     for x in range(width):
#         if (x, y) in node_grid:
#             node = node_grid[(x, y)]
#             if len(node.connections) > 2:
#                 print("+", end="")
#             else:
#                 print(node_grid[(x, y)], end="")
#         else:
#             print(grid[y][x], end="")
#     print()
# print(len(nodes))
# total = 0
# for node in nodes:
#     if len(node.connections) > 2:
#         total += 1
# print(total)

best: int = 0
stack: List[Tuple[Node, Set[Node]]] = [(start, set([start]))]
while len(stack) > 0:
    cur, path = stack.pop()
    if cur == end:
        length = sum([len(n.points) for n in path]) - 1
        if length > best:
            best = length
    for other in cur.connections:
        if not other in path:
            stack.append((other, path | set([other])))
print("!!", best, "!!")