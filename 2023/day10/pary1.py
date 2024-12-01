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

steps = 1
while True:
    for i in range(2):
        if type(maze[curs[i].y][curs[i].x]) is int:
            print(steps)
            exit(0)

        dirs = get_dirs(curs[i])
        dirs.remove(froms[i])
        dir = dirs.pop()
        maze[curs[i].y][curs[i].x] = steps
        curs[i] = curs[i].translate(dir)
        froms[i] = flip(dir)
    steps += 1
