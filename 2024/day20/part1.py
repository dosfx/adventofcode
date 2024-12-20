from collections import deque
from aoc_lib import DIRECTIONS, DOWN, LEFT, RIGHT, UP, StrGrid, Vector2


grid = StrGrid.from_file("input.txt")
start = next(grid.findp("S"))
end = next(grid.findp("E"))
grid.setp(end, ".")


def solve() -> dict[Vector2, int]:
    length = 0
    visited = dict[Vector2, int]()
    queue = deque([start])
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur in visited:
                continue
            visited[cur] = length
            if cur == end:
                return visited
            for d in DIRECTIONS:
                nextp = cur + d
                if grid.atp_none(nextp) != ".":
                    continue
                queue.append(cur + d)
        length += 1
    raise Exception()


costs = solve()
no_cheats = costs[end]
count = 0
for p in grid.findp("#"):
    up = p + UP
    down = p + DOWN
    if up in costs and down in costs:
        diff = abs(costs[up] - costs[down]) - 2
        if diff >= 100:
            count += 1
    left = p + LEFT
    right = p + RIGHT
    if left in costs and right in costs:
        diff = abs(costs[left] - costs[right]) - 2
        if diff >= 100:
            count += 1

print(count)
