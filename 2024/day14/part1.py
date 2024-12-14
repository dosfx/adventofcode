import re
from typing import cast

from aoc_lib import Vector2

with open("input.txt") as file:
    robots: list[tuple[Vector2, Vector2]] = []
    for line in file.readlines():
        m = cast(re.Match[str], re.match(
            r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line))
        p = Vector2(int(m.group(1)), int(m.group(2)))
        v = Vector2(int(m.group(3)), int(m.group(4)))
        robots.append((p, v))

width = 101
height = 103


def visualize(positions: list[Vector2], w: int, h: int) -> None:
    counts: dict[Vector2, int] = {}
    for p in positions:
        counts[p] = counts.get(p, 0) + 1
    for y in range(h):
        for x in range(w):
            p = Vector2(x, y)
            if p in counts:
                print(str(counts[p]), end="")
            else:
                print(".", end="")
        print()


finals = [
    (p + (v * 100)).mod2(width, height)
    for p, v in robots
]

half_width = width // 2
half_height = height // 2
top_left: list[Vector2] = []
top_right: list[Vector2] = []
bot_left: list[Vector2] = []
bot_right: list[Vector2] = []
for p in finals:
    if p.x < half_width:
        if p.y < half_height:
            top_left.append(p)
        elif p.y > half_height:
            top_right.append(p)
    elif p.x > half_width:
        if p.y < half_height:
            bot_left.append(p)
        elif p.y > half_height:
            bot_right.append(p)


print(
    len(top_left) *
    len(top_right) *
    len(bot_left) *
    len(bot_right)
)