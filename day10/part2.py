from dataclasses import dataclass
from enum import Enum
from typing import Dict, Set

class Dirs(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

@dataclass
class Point:
    x: int
    y: int

    def translate(self, dir: Dirs) -> "Point":
        if dir == Dirs.Up:
            return Point(self.x, self.y - 1)
        if dir == Dirs.Down:
            return Point(self.x, self.y + 1)
        if dir == Dirs.Left:
            return Point(self.x - 1, self.y)
        return Point(self.x + 1, self.y)

maze = []
with open("input.txt") as file:
    for i,line in enumerate(file.readlines()):
        maze.append(list(line.strip()))
        s = line.find("S")
        if s >= 0:
            start = Point(s, i)

height = len(maze)
width = len(maze[0])

dir_map: Dict[str, Set[Dirs]] = {
    "|": set([Dirs.Up, Dirs.Down]),
    "-": set([Dirs.Left, Dirs.Right]),
    "L": set([Dirs.Up, Dirs.Right]),
    "F": set([Dirs.Down, Dirs.Right]),
    "7": set([Dirs.Down, Dirs.Left]),
    "J": set([Dirs.Up, Dirs.Left]),
}

def get_dirs(p: Point) -> Set[Dirs]:
    if 0 <= p.x and p.x < width and 0 <= p.y and p.y <= height:
        c = maze[p.y][p.x]
        if c in dir_map:
            return dir_map[c].copy()
    return set()

def flip(dir) -> Dirs:
    if dir == Dirs.Up:
        return Dirs.Down
    if dir == Dirs.Down:
        return Dirs.Up
    if dir == Dirs.Left:
        return Dirs.Right
    return Dirs.Left

curs = []
froms = []
for dir in Dirs:
    temp = start.translate(dir)
    if flip(dir) in get_dirs(temp):
        curs.append(temp)
        froms.append(flip(dir))
assert len(curs) == 2

start_dirs = set([flip(d) for d in froms])
for c,dirs in dir_map.items():
    if dirs == start_dirs:
        maze[start.y][start.x] = c
        break

is_maze = [[False for _ in range(width)] for _ in range(height)]
is_maze[start.y][start.x] = True

while True:
    for i in range(2):
        if is_maze[curs[i].y][curs[i].x]:
            break

        dirs = get_dirs(curs[i])
        dirs.remove(froms[i])
        dir = dirs.pop()
        is_maze[curs[i].y][curs[i].x] = True
        curs[i] = curs[i].translate(dir)
        froms[i] = flip(dir)
    else:
        continue
    break

ups = set(["L", "J"])
downs = set(["F", "7"])
inside = 0
for y in range(height):
    count = 0
    hori = None
    for x in range(width):
        c = maze[y][x]
        if is_maze[y][x]:
            if c == "|":
                assert hori is None, (x, y)
                count += 1
            elif c in ups:
                if hori is None:
                    hori = c
                else:
                    if hori in downs:
                        count += 1
                    hori = None
            elif c in downs:
                if hori is None:
                    hori = c
                else:
                    if hori in ups:
                        count += 1
                    hori = None
            elif c == "-":
                assert hori is not None, (x, y)
            else:
                assert False, (x, y)
        else:
            assert hori is None, (x, y)
            if count % 2 == 1:
                inside += 1
                maze[y][x] = "I"
            else:
                maze[y][x] = "O"

print(inside)

# for y in range(height):
#     for x in range(width):
#         print(maze[y][x], end=" ")
#     print()