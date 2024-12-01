from typing import List, Set, Tuple

Point = Tuple[int, int]

with open("input.txt") as file:
    grid: List[List[str]] = []
    for y,line in enumerate(file.readlines()):
        grid.append([c for c in line.strip()])
size = len(grid)
start = size // 2
grid[start][start] = "."

def dump(steps: List[Point]):
    print(len(steps))
    for y in range(size):
        for x in range(size):
            print("O" if (x, y) in steps else grid[y][x], end="")
        print()

def can_step(x, y) -> bool:
    if x < 0 or size <= x or y < 0 or size <= y:
        return False
    return grid[y][x] == "."

def walk(start: Point, steps: int) -> int:
    parity = steps % 2
    reach: List[Point] = []
    seen: Set[Point] = set()
    last = [start]
    for i in range(steps):
        cur = []
        for x, y in last:
            for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if p in seen:
                    continue
                seen.add(p)
                if can_step(*p):
                    cur.append(p)
                    if i % 2 != parity:
                        reach.append(p)
        last = cur
    # dump(reach)
    return len(reach)

size1 = size - 1
full = walk((start, start), size)
full_flip = walk((start, start), size1)
top_tip = walk((start, size1), size1)
bot_tip = walk((start, 0), size1)
left_tip = walk((size1, start), size1)
right_tip = walk((0, start), size1)
top_left_big = walk((size1, size1), size1 + start)
top_left_little = walk((size1, size1), start - 1)
top_right_big = walk((0, size1), size1 + start)
top_right_little = walk((0, size1), start - 1)
bot_left_big = walk((size1, 0), size1 + start)
bot_left_little = walk((size1, 0), start - 1)
bot_right_big = walk((0, 0), size1 + start)
bot_right_little = walk((0, 0), start - 1)

# steps = start + (3 * size)
# print(steps)
steps = 26501365
radius = (steps - start) // size
total = 0
flip_rings = radius // 2
flip_count = (2 * flip_rings) ** 2
full_rings = flip_rings + radius % 2
full_count = ((2 * full_rings) - 1) ** 2
total += flip_count * full_flip
total += full_count * full
total += radius * (top_left_little + top_right_little + bot_left_little + bot_right_little)
total += (radius - 1) * (top_left_big + top_right_big + bot_left_big + bot_right_big)
total += top_tip + bot_tip + left_tip + right_tip
print(total)