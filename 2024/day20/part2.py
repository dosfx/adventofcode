from collections import deque
from aoc_lib import DIRECTIONS, StrGrid, Vector2


grid = StrGrid.from_file("input.txt")
start = next(grid.findp("S"))
end = next(grid.findp("E"))
grid.setp(start, ".")
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
cheats = dict[tuple[Vector2, Vector2], int]()


def cheat(start: Vector2) -> None:
    length = 0
    visited = set[Vector2]()
    queue = deque(start.directions())
    while queue and length < 20:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            if grid.atp_none(cur) == ".":
                diff = costs[start] - costs[cur]
                if diff < 0:
                    cheats[(start, cur)] = -diff - length - 1
                else:
                    cheats[(cur, start)] = diff - length - 1
            for d in cur.directions():
                if grid.containsp(d):
                    queue.append(d)
        length += 1


no_cheats = costs[end]
for p in grid.findp("."):
    cheat(p)

counts = dict[int, int]()
for diff in cheats.values():
    counts[diff] = counts.get(diff, 0) + 1

count = 0
for diff in sorted(counts.keys(), reverse=True):
    if diff < 100:
        break
    count += counts[diff]
print(count)
